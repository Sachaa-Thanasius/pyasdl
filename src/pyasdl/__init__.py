"""A library for compiling and generating code for a dialect of Abstract Syntax Description Language (ASDL). It reads
ASDL descriptions and writes corresponding Python class definitions.

Much of the documentation and code is copied from or heavily based on CPython's ASDL parser implementation [1]_.

Notes
-----
The grammar being used for parsing ASDL is based on Figure 1 of the original ASDL paper [2]_, but with extensions to
support a) modules and b) attributes after a product.

Words starting with capital letters are terminals. Literal tokens are in "double quotes". Others are non-terminals.

..  code-block:: ebnf

    module        = "module" id "{" [definitions] "}"
    definitions   = { TypeId "=" type }
    type          = product | sum
    product       = fields ["attributes" fields]
    sum           = constructor { "|" constructor } ["attributes" fields]
    constructor   = ConstructorId [fields]
    fields        = "(" { field, "," } field ")"
    field         = TypeId ["?" | "*"] [id]
    id            = TypeId | ConstructorId

References
----------
..  [1] https://github.com/python/cpython/blob/3.13/Parser/asdl.py
..  [2] Wang, D. C., Appel, A. W., Korn, J. L., & Serra, C. S. (1997). The Zephyr abstract syntax description
    language. In Proceedings of the conference on domain-specific languages, October 15-17, 1997, Santa Barbara,
    California (pp. 213-227). Usenix Association.
"""

from __future__ import annotations

import sys
from collections import deque
from collections.abc import Generator, Iterable, Iterator
from enum import Enum, auto
from io import StringIO
from types import GeneratorType
from typing import TYPE_CHECKING, Any, Optional, Union


# Use a shim to avoid a runtime dependency on typing-extensions.
if sys.version_info >= (3, 10):
    from typing import TypeAlias
elif TYPE_CHECKING:
    from typing_extensions import TypeAlias
else:

    class TypeAlias:
        """Placeholder for ``typing.TypeAlias``."""

        __module__ = "typing"


# ============================================================================
# region -------- Exceptions --------
# ============================================================================


class ASDLSyntaxError(Exception):
    """Exception that's raised when a parsing error is encountered."""

    def __init__(self, msg: str, lineno: Optional[int] = None):
        super().__init__()
        self.msg = msg
        self.lineno = lineno or "<unknown>"

    def __str__(self):
        return f"Syntax error on line {self.lineno}: {self.msg}"


# endregion


# ============================================================================
# region -------- Tokenizer --------
# ============================================================================


class TokenKind(Enum):
    """The kinds of tokens that an ASDL specification can contain."""

    # fmt: off
    CONSTRUCTOR_ID  = auto()
    TYPE_ID         = auto()
    EQUALS          = auto()
    COMMA           = auto()
    QUESTION        = auto()
    PIPE            = auto()
    ASTERISK        = auto()
    LPAREN          = auto()
    RPAREN          = auto()
    LBRACE          = auto()
    RBRACE          = auto()
    # fmt: on


OPERATOR_TOKEN_TABLE = {
    "=": TokenKind.EQUALS,
    ",": TokenKind.COMMA,
    "?": TokenKind.QUESTION,
    "|": TokenKind.PIPE,
    "(": TokenKind.LPAREN,
    ")": TokenKind.RPAREN,
    "*": TokenKind.ASTERISK,
    "{": TokenKind.LBRACE,
    "}": TokenKind.RBRACE,
}


class Token:
    __slots__ = ("kind", "value", "lineno")

    def __init__(self, kind: TokenKind, value: str, lineno: int):
        self.kind = kind
        self.value = value
        self.lineno = lineno

    def __repr__(self):
        return f"{self.__class__.__name__}(kind={self.kind!r}, value={self.value!r}, lineno={self.lineno})"


def tokenize(source: str) -> Generator[Token]:
    """Tokenize a source.

    Yields
    ------
    Token
        An token representation, which holds the token kind, value, and line number.

    Raises
    ------
    ASDLSyntaxError
        If something unknown is encountered during tokenization.
    """

    for line_no, line in enumerate(source.splitlines(), start=1):
        col_no = 0

        while col_no < len(line):
            char = line[col_no]

            # Discard whitespace.
            if char.isspace():
                col_no += 1

            # Capture identifiers.
            elif char.isalpha():
                id_start = col_no
                col_no += 1

                # Find the end of the identifier. Default to the end of the line.
                for idx in range(id_start + 1, len(line)):
                    if not (line[idx].isalpha() or line[idx] == "_"):
                        col_no = idx
                        break
                else:
                    col_no = len(line)

                if char.isupper():
                    id_kind = TokenKind.CONSTRUCTOR_ID
                else:
                    id_kind = TokenKind.TYPE_ID

                yield Token(id_kind, line[id_start:col_no], line_no)

            # Discard the line from the comment onwards.
            elif line.startswith("--", col_no):
                break

            # Capture operators.
            elif (op_kind := OPERATOR_TOKEN_TABLE.get(char)) is not None:
                # Operators can only be 1 character long.
                col_no += 1
                yield Token(op_kind, char, line_no)

            # Panic if we encounter something unknown.
            else:
                msg = f"Invalid operator {char}"
                raise ASDLSyntaxError(msg, line_no)


# endregion


# ============================================================================
# region -------- Meta-AST --------
#
# Node classes into which the ASDL description is parsed. Note: this is a
# "meta-AST". ASDL files (such as Python.asdl) describe the AST structure used
# by a programming language. But ASDL files themselves need to be parsed. This
# module parses ASDL files and uses a simple AST to represent them. See the
# EBNF at the top of the file to understand the logical connection between the
# various node types.
# ============================================================================


class FieldQuantifier(Enum):
    SEQ = auto()
    OPT = auto()


class AST:
    __slots__ = ("__weakref__",)
    __match_args__ = _fields = ()


class Module(AST):
    __match_args__ = __slots__ = _fields = ("name", "dfns")

    def __init__(self, name: str, dfns: list[Type] = ...):
        self.name = name
        self.dfns = dfns if (dfns is not ...) else []


class Type(AST):
    __match_args__ = __slots__ = _fields = ("name", "value")

    def __init__(self, name: str, value: Union[Product, Sum]):
        self.name = name
        self.value = value


class Sum(AST):
    __match_args__ = __slots__ = _fields = ("types", "attributes")

    def __init__(self, types: list[Constructor] = ..., attributes: list[Field] = ...):
        self.types = types if (types is not ...) else []
        self.attributes = attributes if (attributes is not ...) else []


class Product(AST):
    __match_args__ = __slots__ = _fields = ("fields", "attributes")

    def __init__(self, fields: list[Field] = ..., attributes: list[Field] = ...):
        self.fields = fields if (fields is not ...) else []
        self.attributes = attributes if (attributes is not ...) else []


class Constructor(AST):
    __match_args__ = __slots__ = _fields = ("name", "fields")

    def __init__(self, name: str, fields: list[Field] = ...):
        self.name = name
        self.fields = fields if (fields is not ...) else []


class Field(AST):
    __match_args__ = __slots__ = _fields = ("type", "name", "quantifier")

    def __init__(
        self,
        type: str,  # noqa: A002
        name: Optional[str] = None,
        quantifier: Optional[FieldQuantifier] = None,
    ):
        self.type = type
        self.name = name
        self.quantifier = quantifier

    def __str__(self):
        if self.quantifier is FieldQuantifier.SEQ:
            extra = "*"
        elif self.quantifier is FieldQuantifier.OPT:
            extra = "?"
        else:
            extra = ""

        return f"{self.type}{extra} {self.name}"


# endregion


# ============================================================================
# region -------- Meta-AST helpers --------
#
# Helper functions and classes for operating on the meta-AST nodes.
# ============================================================================


def iter_child_nodes(node: AST) -> Generator[AST]:
    """Yield all direct child nodes of a given node.

    This includes all fields that are nodes and all items of fields that are lists of nodes.
    """

    for node_field in node._fields:
        potential_subnode = getattr(node, node_field)

        if isinstance(potential_subnode, AST):
            yield potential_subnode

        elif isinstance(potential_subnode, list):
            for subsub in potential_subnode:  # pyright: ignore [reportUnknownVariableType]
                if isinstance(subsub, AST):
                    yield subsub


def walk(node: AST) -> Generator[AST]:
    """Walk through an AST, breadth first."""

    stack: deque[AST] = deque([node])
    while stack:
        curr_node = stack.popleft()
        stack.extend(iter_child_nodes(curr_node))
        yield curr_node


class NodeVisitor:
    """Generic tree visitor for the meta-AST that describes ASDL.

    Notes
    -----
    The generator-based implemention is based on a talk by David Beazley called "Generators: The Final Frontier".
    """

    def _visit(self, node: AST) -> Generator[Any, Any, Any]:
        """Wrapper for visit methods to ensure visit() only deals with generators."""

        result: Any = getattr(self, f"visit_{node.__class__.__name__}", self.generic_visit)(node)
        if isinstance(result, GeneratorType):
            result = yield from result
        return result

    def visit(self, node: AST) -> Any:
        """Visit a node."""

        stack: deque[Generator[Any, Any, Any]] = deque([self._visit(node)])
        result: Any = None
        exception: Optional[BaseException] = None

        while stack:
            try:
                if exception is not None:
                    node = stack[-1].throw(exception)
                else:
                    node = stack[-1].send(result)
            except StopIteration as exc:  # noqa: PERF203 # This loop cannot avoid exceptions as control flow.
                stack.pop()
                result = exc.value
            except BaseException as exc:  # noqa: BLE001 # The exception is propogated.
                stack.pop()
                exception = exc
            else:
                stack.append(self._visit(node))
                result = None
                exception = None

        if exception is not None:
            raise exception
        else:
            return result

    def generic_visit(self, node: AST) -> Generator[AST, Any, Any]:
        """Called if no explicit visitor function exists for a node."""

        yield from iter_child_nodes(node)


# endregion


# ============================================================================
# region -------- Parser --------
#
# A parser for ASDL definition files. It reads in an ASDL description and
# parses it into an AST that describes it.
#
# TODO: For fun, make this iterative with generators instead of recursive.
# ============================================================================


TOKEN_TO_FIELD_QUANTIFIER = {
    TokenKind.ASTERISK: FieldQuantifier.SEQ,
    TokenKind.QUESTION: FieldQuantifier.OPT,
}


class ASDLParser:
    """Parser for ASDL files.

    This is a simple recursive descent parser that acts on an iteratable of tokens.
    """

    _id_kinds = (TokenKind.CONSTRUCTOR_ID, TokenKind.TYPE_ID)

    cur_token: Optional[Token]

    def __init__(self):
        self._tokenizer: Iterator[Token] = None
        self.cur_token = None

    # region ---- Parsing helpers -----

    def _advance(self) -> Optional[str]:
        """Return the value of the current token and read the next one into self.cur_token."""

        cur_val = None if (self.cur_token is None) else self.cur_token.value
        self.cur_token = next(self._tokenizer, None)
        return cur_val

    def _match(self, kind: Union[TokenKind, tuple[TokenKind, ...]]) -> str:
        """The 'match' primitive of RD parsers.

        *   Verifies that the current token is of the given kind (kind can be a tuple, in which the kind must match one
            of its members).
        *   Returns the value of the current token
        *   Reads in the next token
        """

        if (isinstance(kind, tuple) and self.cur_token.kind in kind) or self.cur_token.kind is kind:
            value = self.cur_token.value
            self._advance()
            return value
        else:
            msg = f"Unmatched {kind} (found {self.cur_token.kind})"
            raise ASDLSyntaxError(msg, self.cur_token.lineno)

    def _at_keyword(self, keyword: str) -> bool:
        """Check if the current token is an identifier and matches the given keyword.

        It does not advance to the next token.
        """

        return self.cur_token.kind == TokenKind.TYPE_ID and self.cur_token.value == keyword

    # endregion

    # region ---- Parsing rules ----

    def parse(self, tokens: Iterable[Token]) -> Module:
        """Parse the ASDL token stream and return an AST with a Module root."""

        self._tokenizer = iter(tokens)
        self._advance()
        return self.parse_module()

    def parse_module(self) -> Module:
        if not self._at_keyword("module"):
            msg = f'Expected "module" (found {self.cur_token.value})'
            raise ASDLSyntaxError(msg, self.cur_token.lineno)

        self._advance()
        name = self._match(self._id_kinds)
        self._match(TokenKind.LBRACE)
        defs = self.parse_definitions()
        self._match(TokenKind.RBRACE)
        return Module(name, defs)

    def parse_definitions(self) -> list[Type]:
        defs: list[Type] = []

        while self.cur_token.kind is TokenKind.TYPE_ID:
            typename = self._advance()
            self._match(TokenKind.EQUALS)
            type_ = self.parse_type()
            defs.append(Type(typename, type_))

        return defs

    def parse_type(self) -> Union[Product, Sum]:
        if self.cur_token.kind is TokenKind.LPAREN:
            # If we see a "(", it's a product
            return self.parse_product()
        else:
            # Otherwise, it's a sum.
            return self.parse_sum()

    def parse_sum(self) -> Sum:
        # Look for ConstructorId.
        sumlist = [Constructor(self._match(TokenKind.CONSTRUCTOR_ID), self.parse_optional_fields())]
        while self.cur_token.kind is TokenKind.PIPE:
            # More constructors
            self._advance()
            sumlist.append(Constructor(self._match(TokenKind.CONSTRUCTOR_ID), self.parse_optional_fields()))
        return Sum(sumlist, self.parse_optional_attributes())

    def parse_product(self) -> Product:
        return Product(self.parse_fields(), self.parse_optional_attributes())

    def parse_fields(self) -> list[Field]:
        fields: list[Field] = []
        self._match(TokenKind.LPAREN)

        while self.cur_token.kind is TokenKind.TYPE_ID:
            typename = self._advance()
            field_quantifier = self.parse_optional_field_quantifier()
            id_ = self._advance() if self.cur_token.kind in self._id_kinds else None
            fields.append(Field(typename, id_, field_quantifier))
            if self.cur_token.kind is TokenKind.RPAREN:
                break
            elif self.cur_token.kind is TokenKind.COMMA:
                self._advance()

        self._match(TokenKind.RPAREN)
        return fields

    def parse_optional_fields(self) -> list[Field]:
        if self.cur_token.kind is TokenKind.LPAREN:
            return self.parse_fields()
        else:
            return []

    def parse_optional_attributes(self) -> list[Field]:
        if self._at_keyword("attributes"):
            self._advance()
            return self.parse_fields()
        else:
            return []

    def parse_optional_field_quantifier(self) -> Optional[FieldQuantifier]:
        quantifier = TOKEN_TO_FIELD_QUANTIFIER.get(self.cur_token.kind)
        if quantifier is not None:
            self._advance()
        return quantifier

    # endregion


def parse(source: str) -> Module:
    """Parse ASDL from the given buffer and return a Module node describing it."""

    parser = ASDLParser()
    return parser.parse(tokenize(source))


# endregion


# ============================================================================
# region -------- Code generator --------
#
# A generator that takes in a parse tree representing an ASDL description and
# outputs Python code.
# ============================================================================


_ASTGen: TypeAlias = Generator[AST, Any, Any]

ASDL_TYPE_TO_PYTHON_TYPE = {
    "identifier": "str",
    "string": "str",
    "int": "int",
    "constant": "object",
}

ASDL_TYPES = set(ASDL_TYPE_TO_PYTHON_TYPE)


class Checker(NodeVisitor):
    """A visitor that checks a parsed ASDL tree for correctness. Errors are accumulated."""

    constructors: dict[str, str]
    types: dict[str, list[str]]
    error_messages: list[str]
    parent_type_name: str

    def __init__(self):
        super().__init__()
        self.constructors = {}
        self.types = {}
        self.error_messages = []
        self.parent_type_name = ""

    def visit_Type(self, node: Type) -> _ASTGen:
        self.parent_type_name = node.name
        return self.generic_visit(node)

    def visit_Constructor(self, node: Constructor) -> _ASTGen:
        parent_name = self.parent_type_name
        self.parent_type_name = node.name

        try:
            conflict = self.constructors[self.parent_type_name]
        except KeyError:
            self.constructors[self.parent_type_name] = parent_name
        else:
            self.error_messages.append(f"Redefinition of constructor {self.parent_type_name}")
            self.error_messages.append(f"Defined in {conflict} and {parent_name}")

        return self.generic_visit(node)

    def visit_Field(self, field: Field) -> None:
        self.types.setdefault(field.type, []).append(self.parent_type_name)


def check_tree(mod: Module) -> None:
    """Check the parsed ASDL tree for correctness.

    Raises
    ------
    ASDLSyntaxError
        If the tree has any type name conflicts or undefined types.
    """

    checker = Checker()
    checker.visit(mod)

    error_messages = checker.error_messages

    module_types = {type_.name for type_ in mod.dfns}
    expected_types = ASDL_TYPES | module_types

    for type_name in checker.types:
        if type_name not in expected_types:
            uses = ", ".join(checker.types[type_name])
            error_messages.append(f"Undefined type {type_name}, used in {uses}")

    if error_messages:
        raise ASDLSyntaxError("\n".join(error_messages))


class _AttributeStatements:
    __slots__ = ("init_params", "init_body_stmts")

    def __init__(self, init_params: list[str], body_stmts: list[str]):
        self.init_params = init_params
        self.init_body_stmts = body_stmts


class PythonCodeGenerator(NodeVisitor):
    """Visitor that generates Python code based on the given AST into an internal string buffer."""

    # NOTE: The calls to self.write might incur unnecessary overhead, but no benchmarking has been done yet.

    def __init__(self):
        self.buffer = StringIO()

        self.parent_type_name: str = ""
        self.parent_type_attributes: _AttributeStatements | None = None

    def __enter__(self):
        return self

    def __exit__(self, *_exc_info: object):
        self.buffer.close()

    def write(self, s: str = "", /, *, end: str = "\n") -> None:
        """Write a string to the internal buffer.

        Parameters
        ----------
        s: str, default=""
            The string to write. Defaults to the empty string.
        end: str, default="\\n"
            What should be added to the end of the given string. Defaults to a newline.
        """

        self.buffer.write(f"{s}{end}")

    def writelines(self, *lines: str, end: str = "\n") -> None:
        """Write multiple strings to the internal buffer.

        Parameters
        ----------
        end: str, default="\\n"
            What should be added to the end of each string. Defaults to a newline.
        """

        self.buffer.writelines(f"{line}{end}" for line in lines)

    def get_value(self) -> str:
        """Get the generated code."""

        return self.buffer.getvalue()

    def visit(self, node: AST) -> Any:
        """Construct the import statements and base class before starting the regular tree traversal."""

        # Imports
        self.writelines(
            "from __future__ import annotations",
            "",
            "from typing import Optional",
            "",
            "",
        )

        # Base class
        self.writelines(
            "class AST:",
            "    __match_args__ = ()",
            "    _fields = ()",
            "",
            "",
        )

        return super().visit(node)

    def visit_Type(self, node: Type) -> _ASTGen:
        self.parent_type_name = node.name
        return self.generic_visit(node)

    @staticmethod
    def _build_init_param_from_field(field: Field) -> str:
        param_name = f"{field.name}: "
        param_annotation = ASDL_TYPE_TO_PYTHON_TYPE.get(field.type, field.type)

        if field.quantifier is FieldQuantifier.SEQ:
            param_annotation = f"list[{param_annotation}]"

        elif field.quantifier is FieldQuantifier.OPT:
            param_annotation = f"Optional[{param_annotation}]"

        return "".join((param_name, param_annotation))

    def visit_Sum(self, node: Sum) -> _ASTGen:
        init_params = ["self"]
        init_body: list[str] = []

        if node.attributes:
            attribute_init_params = ["*"]
            attribute_init_body: list[str] = []

            for attr in node.attributes:
                attribute_init_params.append(self._build_init_param_from_field(attr))
                attribute_init_body.append(f"self.{attr.name} = {attr.name}")

            init_params.extend(attribute_init_params)
            init_body.extend(attribute_init_body)

            saved_attributes = _AttributeStatements(attribute_init_params, attribute_init_body)
        else:
            saved_attributes = None

        # Construct the sum class.
        self.writelines(
            f"class {self.parent_type_name}(AST):",
            "    __match_args__ = ()",
            "    _fields = ()",
            "",
        )

        # Only construct an __init__ if it's going to do something.
        if len(init_params) > 1 or init_body:
            sig = ", ".join(init_params)
            self.write(f"    def __init__({sig}) -> None:")

            for body_stmt in init_body:
                self.write(f"        {body_stmt}")

            self.write()

        self.write()

        self.parent_type_attributes = saved_attributes
        return self.generic_visit(node)

    def visit_Product(self, node: Product) -> _ASTGen:
        match_args_and_field_names: list[str] = []
        init_params = ["self"]
        init_body: list[str] = []

        if node.fields:
            for field in node.fields:
                match_args_and_field_names.append(repr(field.name))
                init_params.append(self._build_init_param_from_field(field))
                init_body.append(f"self.{field.name} = {field.name}")

        if node.attributes:
            attribute_init_params = ["*"]
            attribute_init_body: list[str] = []

            for attr in node.attributes:
                attribute_init_params.append(self._build_init_param_from_field(attr))
                attribute_init_body.append(f"self.{attr.name} = {attr.name}")

            init_params.extend(attribute_init_params)
            init_body.extend(attribute_init_body)

            saved_attributes = _AttributeStatements(attribute_init_params, attribute_init_body)
        else:
            saved_attributes = None

        match_args_and_fields = ", ".join(match_args_and_field_names)

        # Construct the product class.
        self.writelines(
            f"class {self.parent_type_name}(AST):",
            f"    __match_args__ = ({match_args_and_fields})",
            f"    _fields = ({match_args_and_fields})",
            "",
        )

        # Only construct an __init__ if it's going to do something.
        if len(init_params) > 1 or init_body:
            sig = ", ".join(init_params)
            self.write(f"    def __init__({sig}) -> None:")

            for body_stmt in init_body:
                self.write(f"        {body_stmt}")

            self.write()

        self.write()

        self.parent_type_attributes = saved_attributes
        return self.generic_visit(node)

    def visit_Constructor(self, node: Constructor) -> None:
        match_args_and_field_names: list[str] = []
        init_params = ["self"]
        init_body: list[str] = []

        if node.fields:
            for field in node.fields:
                match_args_and_field_names.append(repr(field.name))
                init_params.append(self._build_init_param_from_field(field))
                init_body.append(f"self.{field.name} = {field.name}")

        if self.parent_type_attributes:
            init_params.extend(self.parent_type_attributes.init_params)
            init_body.extend(self.parent_type_attributes.init_body_stmts)

        match_args_and_fields = ", ".join(match_args_and_field_names)

        # Construct the concrete class.
        self.writelines(
            f"class {node.name}({self.parent_type_name}):",
            f"    __match_args__ = ({match_args_and_fields})",
            f"    _fields = ({match_args_and_fields})",
            "",
        )

        # Only construct an __init__ if it's going to do something.
        if len(init_params) > 1 or init_body:
            sig = ", ".join(init_params)
            self.write(f"    def __init__({sig}) -> None:")

            for body_stmt in init_body:
                self.write(f"        {body_stmt}")

            self.write()

        self.write()


def generate_code(source: str) -> str:
    """Generate Python code based on the given ASDL description."""

    tree = parse(source)
    check_tree(tree)

    with PythonCodeGenerator() as code_generator:
        code_generator.visit(tree)
        return code_generator.get_value()


# endregion
