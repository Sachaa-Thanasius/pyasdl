from __future__ import annotations

from typing import Optional


class AST:
    __match_args__ = ()
    _fields = ()

class mod(AST):
    __match_args__ = ()
    _fields = ()


class Module(mod):
    __match_args__ = ('body', 'type_ignores')
    _fields = ('body', 'type_ignores')

    def __init__(self, body: list[stmt] = ..., type_ignores: list[type_ignore] = ...) -> None:
        self.body = body if (body is not ...) else []
        self.type_ignores = type_ignores if (type_ignores is not ...) else []

class Interactive(mod):
    __match_args__ = ('body')
    _fields = ('body')

    def __init__(self, body: list[stmt] = ...) -> None:
        self.body = body if (body is not ...) else []

class Expression(mod):
    __match_args__ = ('body')
    _fields = ('body')

    def __init__(self, body: expr) -> None:
        self.body = body

class FunctionType(mod):
    __match_args__ = ('argtypes', 'returns')
    _fields = ('argtypes', 'returns')

    def __init__(self, argtypes: list[expr] = ..., returns: expr) -> None:
        self.argtypes = argtypes if (argtypes is not ...) else []
        self.returns = returns

class stmt(AST):
    __match_args__ = ()
    _fields = ()

    def __init__(self, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class FunctionDef(stmt):
    __match_args__ = ('name', 'args', 'body', 'decorator_list', 'returns', 'type_comment', 'type_params')
    _fields = ('name', 'args', 'body', 'decorator_list', 'returns', 'type_comment', 'type_params')

    def __init__(self, name: str, args: arguments, body: list[stmt] = ..., decorator_list: list[expr] = ..., returns: Optional[expr] = None, type_comment: Optional[str] = None, type_params: list[type_param] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.name = name
        self.args = args
        self.body = body if (body is not ...) else []
        self.decorator_list = decorator_list if (decorator_list is not ...) else []
        self.returns = returns
        self.type_comment = type_comment
        self.type_params = type_params if (type_params is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class AsyncFunctionDef(stmt):
    __match_args__ = ('name', 'args', 'body', 'decorator_list', 'returns', 'type_comment', 'type_params')
    _fields = ('name', 'args', 'body', 'decorator_list', 'returns', 'type_comment', 'type_params')

    def __init__(self, name: str, args: arguments, body: list[stmt] = ..., decorator_list: list[expr] = ..., returns: Optional[expr] = None, type_comment: Optional[str] = None, type_params: list[type_param] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.name = name
        self.args = args
        self.body = body if (body is not ...) else []
        self.decorator_list = decorator_list if (decorator_list is not ...) else []
        self.returns = returns
        self.type_comment = type_comment
        self.type_params = type_params if (type_params is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class ClassDef(stmt):
    __match_args__ = ('name', 'bases', 'keywords', 'body', 'decorator_list', 'type_params')
    _fields = ('name', 'bases', 'keywords', 'body', 'decorator_list', 'type_params')

    def __init__(self, name: str, bases: list[expr] = ..., keywords: list[keyword] = ..., body: list[stmt] = ..., decorator_list: list[expr] = ..., type_params: list[type_param] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.name = name
        self.bases = bases if (bases is not ...) else []
        self.keywords = keywords if (keywords is not ...) else []
        self.body = body if (body is not ...) else []
        self.decorator_list = decorator_list if (decorator_list is not ...) else []
        self.type_params = type_params if (type_params is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Return(stmt):
    __match_args__ = ('value')
    _fields = ('value')

    def __init__(self, value: Optional[expr] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.value = value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Delete(stmt):
    __match_args__ = ('targets')
    _fields = ('targets')

    def __init__(self, targets: list[expr] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.targets = targets if (targets is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Assign(stmt):
    __match_args__ = ('targets', 'value', 'type_comment')
    _fields = ('targets', 'value', 'type_comment')

    def __init__(self, targets: list[expr] = ..., value: expr, type_comment: Optional[str] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.targets = targets if (targets is not ...) else []
        self.value = value
        self.type_comment = type_comment
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class TypeAlias(stmt):
    __match_args__ = ('name', 'type_params', 'value')
    _fields = ('name', 'type_params', 'value')

    def __init__(self, name: expr, type_params: list[type_param] = ..., value: expr, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.name = name
        self.type_params = type_params if (type_params is not ...) else []
        self.value = value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class AugAssign(stmt):
    __match_args__ = ('target', 'op', 'value')
    _fields = ('target', 'op', 'value')

    def __init__(self, target: expr, op: operator, value: expr, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.target = target
        self.op = op
        self.value = value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class AnnAssign(stmt):
    __match_args__ = ('target', 'annotation', 'value', 'simple')
    _fields = ('target', 'annotation', 'value', 'simple')

    def __init__(self, target: expr, annotation: expr, value: Optional[expr] = None, simple: int, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.target = target
        self.annotation = annotation
        self.value = value
        self.simple = simple
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class For(stmt):
    __match_args__ = ('target', 'iter', 'body', 'orelse', 'type_comment')
    _fields = ('target', 'iter', 'body', 'orelse', 'type_comment')

    def __init__(self, target: expr, iter: expr, body: list[stmt] = ..., orelse: list[stmt] = ..., type_comment: Optional[str] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.target = target
        self.iter = iter
        self.body = body if (body is not ...) else []
        self.orelse = orelse if (orelse is not ...) else []
        self.type_comment = type_comment
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class AsyncFor(stmt):
    __match_args__ = ('target', 'iter', 'body', 'orelse', 'type_comment')
    _fields = ('target', 'iter', 'body', 'orelse', 'type_comment')

    def __init__(self, target: expr, iter: expr, body: list[stmt] = ..., orelse: list[stmt] = ..., type_comment: Optional[str] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.target = target
        self.iter = iter
        self.body = body if (body is not ...) else []
        self.orelse = orelse if (orelse is not ...) else []
        self.type_comment = type_comment
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class While(stmt):
    __match_args__ = ('test', 'body', 'orelse')
    _fields = ('test', 'body', 'orelse')

    def __init__(self, test: expr, body: list[stmt] = ..., orelse: list[stmt] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.test = test
        self.body = body if (body is not ...) else []
        self.orelse = orelse if (orelse is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class If(stmt):
    __match_args__ = ('test', 'body', 'orelse')
    _fields = ('test', 'body', 'orelse')

    def __init__(self, test: expr, body: list[stmt] = ..., orelse: list[stmt] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.test = test
        self.body = body if (body is not ...) else []
        self.orelse = orelse if (orelse is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class With(stmt):
    __match_args__ = ('items', 'body', 'type_comment')
    _fields = ('items', 'body', 'type_comment')

    def __init__(self, items: list[withitem] = ..., body: list[stmt] = ..., type_comment: Optional[str] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.items = items if (items is not ...) else []
        self.body = body if (body is not ...) else []
        self.type_comment = type_comment
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class AsyncWith(stmt):
    __match_args__ = ('items', 'body', 'type_comment')
    _fields = ('items', 'body', 'type_comment')

    def __init__(self, items: list[withitem] = ..., body: list[stmt] = ..., type_comment: Optional[str] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.items = items if (items is not ...) else []
        self.body = body if (body is not ...) else []
        self.type_comment = type_comment
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Match(stmt):
    __match_args__ = ('subject', 'cases')
    _fields = ('subject', 'cases')

    def __init__(self, subject: expr, cases: list[match_case] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.subject = subject
        self.cases = cases if (cases is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Raise(stmt):
    __match_args__ = ('exc', 'cause')
    _fields = ('exc', 'cause')

    def __init__(self, exc: Optional[expr] = None, cause: Optional[expr] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.exc = exc
        self.cause = cause
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Try(stmt):
    __match_args__ = ('body', 'handlers', 'orelse', 'finalbody')
    _fields = ('body', 'handlers', 'orelse', 'finalbody')

    def __init__(self, body: list[stmt] = ..., handlers: list[excepthandler] = ..., orelse: list[stmt] = ..., finalbody: list[stmt] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.body = body if (body is not ...) else []
        self.handlers = handlers if (handlers is not ...) else []
        self.orelse = orelse if (orelse is not ...) else []
        self.finalbody = finalbody if (finalbody is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class TryStar(stmt):
    __match_args__ = ('body', 'handlers', 'orelse', 'finalbody')
    _fields = ('body', 'handlers', 'orelse', 'finalbody')

    def __init__(self, body: list[stmt] = ..., handlers: list[excepthandler] = ..., orelse: list[stmt] = ..., finalbody: list[stmt] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.body = body if (body is not ...) else []
        self.handlers = handlers if (handlers is not ...) else []
        self.orelse = orelse if (orelse is not ...) else []
        self.finalbody = finalbody if (finalbody is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Assert(stmt):
    __match_args__ = ('test', 'msg')
    _fields = ('test', 'msg')

    def __init__(self, test: expr, msg: Optional[expr] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.test = test
        self.msg = msg
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Import(stmt):
    __match_args__ = ('names')
    _fields = ('names')

    def __init__(self, names: list[alias] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.names = names if (names is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class ImportFrom(stmt):
    __match_args__ = ('module', 'names', 'level')
    _fields = ('module', 'names', 'level')

    def __init__(self, module: Optional[str] = None, names: list[alias] = ..., level: Optional[int] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.module = module
        self.names = names if (names is not ...) else []
        self.level = level
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Global(stmt):
    __match_args__ = ('names')
    _fields = ('names')

    def __init__(self, names: list[str] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.names = names if (names is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Nonlocal(stmt):
    __match_args__ = ('names')
    _fields = ('names')

    def __init__(self, names: list[str] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.names = names if (names is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Expr(stmt):
    __match_args__ = ('value')
    _fields = ('value')

    def __init__(self, value: expr, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.value = value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Pass(stmt):
    __match_args__ = ()
    _fields = ()

    def __init__(self, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Break(stmt):
    __match_args__ = ()
    _fields = ()

    def __init__(self, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Continue(stmt):
    __match_args__ = ()
    _fields = ()

    def __init__(self, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class expr(AST):
    __match_args__ = ()
    _fields = ()

    def __init__(self, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class BoolOp(expr):
    __match_args__ = ('op', 'values')
    _fields = ('op', 'values')

    def __init__(self, op: boolop, values: list[expr] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.op = op
        self.values = values if (values is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class NamedExpr(expr):
    __match_args__ = ('target', 'value')
    _fields = ('target', 'value')

    def __init__(self, target: expr, value: expr, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.target = target
        self.value = value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class BinOp(expr):
    __match_args__ = ('left', 'op', 'right')
    _fields = ('left', 'op', 'right')

    def __init__(self, left: expr, op: operator, right: expr, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.left = left
        self.op = op
        self.right = right
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class UnaryOp(expr):
    __match_args__ = ('op', 'operand')
    _fields = ('op', 'operand')

    def __init__(self, op: unaryop, operand: expr, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.op = op
        self.operand = operand
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Lambda(expr):
    __match_args__ = ('args', 'body')
    _fields = ('args', 'body')

    def __init__(self, args: arguments, body: expr, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.args = args
        self.body = body
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class IfExp(expr):
    __match_args__ = ('test', 'body', 'orelse')
    _fields = ('test', 'body', 'orelse')

    def __init__(self, test: expr, body: expr, orelse: expr, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.test = test
        self.body = body
        self.orelse = orelse
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Dict(expr):
    __match_args__ = ('keys', 'values')
    _fields = ('keys', 'values')

    def __init__(self, keys: list[expr] = ..., values: list[expr] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.keys = keys if (keys is not ...) else []
        self.values = values if (values is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Set(expr):
    __match_args__ = ('elts')
    _fields = ('elts')

    def __init__(self, elts: list[expr] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.elts = elts if (elts is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class ListComp(expr):
    __match_args__ = ('elt', 'generators')
    _fields = ('elt', 'generators')

    def __init__(self, elt: expr, generators: list[comprehension] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.elt = elt
        self.generators = generators if (generators is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class SetComp(expr):
    __match_args__ = ('elt', 'generators')
    _fields = ('elt', 'generators')

    def __init__(self, elt: expr, generators: list[comprehension] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.elt = elt
        self.generators = generators if (generators is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class DictComp(expr):
    __match_args__ = ('key', 'value', 'generators')
    _fields = ('key', 'value', 'generators')

    def __init__(self, key: expr, value: expr, generators: list[comprehension] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.key = key
        self.value = value
        self.generators = generators if (generators is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class GeneratorExp(expr):
    __match_args__ = ('elt', 'generators')
    _fields = ('elt', 'generators')

    def __init__(self, elt: expr, generators: list[comprehension] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.elt = elt
        self.generators = generators if (generators is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Await(expr):
    __match_args__ = ('value')
    _fields = ('value')

    def __init__(self, value: expr, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.value = value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Yield(expr):
    __match_args__ = ('value')
    _fields = ('value')

    def __init__(self, value: Optional[expr] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.value = value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class YieldFrom(expr):
    __match_args__ = ('value')
    _fields = ('value')

    def __init__(self, value: expr, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.value = value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Compare(expr):
    __match_args__ = ('left', 'ops', 'comparators')
    _fields = ('left', 'ops', 'comparators')

    def __init__(self, left: expr, ops: list[cmpop] = ..., comparators: list[expr] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.left = left
        self.ops = ops if (ops is not ...) else []
        self.comparators = comparators if (comparators is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Call(expr):
    __match_args__ = ('func', 'args', 'keywords')
    _fields = ('func', 'args', 'keywords')

    def __init__(self, func: expr, args: list[expr] = ..., keywords: list[keyword] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.func = func
        self.args = args if (args is not ...) else []
        self.keywords = keywords if (keywords is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class FormattedValue(expr):
    __match_args__ = ('value', 'conversion', 'format_spec')
    _fields = ('value', 'conversion', 'format_spec')

    def __init__(self, value: expr, conversion: int, format_spec: Optional[expr] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.value = value
        self.conversion = conversion
        self.format_spec = format_spec
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class JoinedStr(expr):
    __match_args__ = ('values')
    _fields = ('values')

    def __init__(self, values: list[expr] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.values = values if (values is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Constant(expr):
    __match_args__ = ('value', 'kind')
    _fields = ('value', 'kind')

    def __init__(self, value: object, kind: Optional[str] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.value = value
        self.kind = kind
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Attribute(expr):
    __match_args__ = ('value', 'attr', 'ctx')
    _fields = ('value', 'attr', 'ctx')

    def __init__(self, value: expr, attr: str, ctx: expr_context, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.value = value
        self.attr = attr
        self.ctx = ctx
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Subscript(expr):
    __match_args__ = ('value', 'slice', 'ctx')
    _fields = ('value', 'slice', 'ctx')

    def __init__(self, value: expr, slice: expr, ctx: expr_context, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.value = value
        self.slice = slice
        self.ctx = ctx
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Starred(expr):
    __match_args__ = ('value', 'ctx')
    _fields = ('value', 'ctx')

    def __init__(self, value: expr, ctx: expr_context, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.value = value
        self.ctx = ctx
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Name(expr):
    __match_args__ = ('id', 'ctx')
    _fields = ('id', 'ctx')

    def __init__(self, id: str, ctx: expr_context, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.id = id
        self.ctx = ctx
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class List(expr):
    __match_args__ = ('elts', 'ctx')
    _fields = ('elts', 'ctx')

    def __init__(self, elts: list[expr] = ..., ctx: expr_context, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.elts = elts if (elts is not ...) else []
        self.ctx = ctx
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Tuple(expr):
    __match_args__ = ('elts', 'ctx')
    _fields = ('elts', 'ctx')

    def __init__(self, elts: list[expr] = ..., ctx: expr_context, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.elts = elts if (elts is not ...) else []
        self.ctx = ctx
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class Slice(expr):
    __match_args__ = ('lower', 'upper', 'step')
    _fields = ('lower', 'upper', 'step')

    def __init__(self, lower: Optional[expr] = None, upper: Optional[expr] = None, step: Optional[expr] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.lower = lower
        self.upper = upper
        self.step = step
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class expr_context(AST):
    __match_args__ = ()
    _fields = ()


class Load(expr_context):
    __match_args__ = ()
    _fields = ()


class Store(expr_context):
    __match_args__ = ()
    _fields = ()


class Del(expr_context):
    __match_args__ = ()
    _fields = ()


class boolop(AST):
    __match_args__ = ()
    _fields = ()


class And(boolop):
    __match_args__ = ()
    _fields = ()


class Or(boolop):
    __match_args__ = ()
    _fields = ()


class operator(AST):
    __match_args__ = ()
    _fields = ()


class Add(operator):
    __match_args__ = ()
    _fields = ()


class Sub(operator):
    __match_args__ = ()
    _fields = ()


class Mult(operator):
    __match_args__ = ()
    _fields = ()


class MatMult(operator):
    __match_args__ = ()
    _fields = ()


class Div(operator):
    __match_args__ = ()
    _fields = ()


class Mod(operator):
    __match_args__ = ()
    _fields = ()


class Pow(operator):
    __match_args__ = ()
    _fields = ()


class LShift(operator):
    __match_args__ = ()
    _fields = ()


class RShift(operator):
    __match_args__ = ()
    _fields = ()


class BitOr(operator):
    __match_args__ = ()
    _fields = ()


class BitXor(operator):
    __match_args__ = ()
    _fields = ()


class BitAnd(operator):
    __match_args__ = ()
    _fields = ()


class FloorDiv(operator):
    __match_args__ = ()
    _fields = ()


class unaryop(AST):
    __match_args__ = ()
    _fields = ()


class Invert(unaryop):
    __match_args__ = ()
    _fields = ()


class Not(unaryop):
    __match_args__ = ()
    _fields = ()


class UAdd(unaryop):
    __match_args__ = ()
    _fields = ()


class USub(unaryop):
    __match_args__ = ()
    _fields = ()


class cmpop(AST):
    __match_args__ = ()
    _fields = ()


class Eq(cmpop):
    __match_args__ = ()
    _fields = ()


class NotEq(cmpop):
    __match_args__ = ()
    _fields = ()


class Lt(cmpop):
    __match_args__ = ()
    _fields = ()


class LtE(cmpop):
    __match_args__ = ()
    _fields = ()


class Gt(cmpop):
    __match_args__ = ()
    _fields = ()


class GtE(cmpop):
    __match_args__ = ()
    _fields = ()


class Is(cmpop):
    __match_args__ = ()
    _fields = ()


class IsNot(cmpop):
    __match_args__ = ()
    _fields = ()


class In(cmpop):
    __match_args__ = ()
    _fields = ()


class NotIn(cmpop):
    __match_args__ = ()
    _fields = ()


class comprehension(AST):
    __match_args__ = ('target', 'iter', 'ifs', 'is_async')
    _fields = ('target', 'iter', 'ifs', 'is_async')

    def __init__(self, target: expr, iter: expr, ifs: list[expr] = ..., is_async: int) -> None:
        self.target = target
        self.iter = iter
        self.ifs = ifs if (ifs is not ...) else []
        self.is_async = is_async

class excepthandler(AST):
    __match_args__ = ()
    _fields = ()

    def __init__(self, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class ExceptHandler(excepthandler):
    __match_args__ = ('type', 'name', 'body')
    _fields = ('type', 'name', 'body')

    def __init__(self, type: Optional[expr] = None, name: Optional[str] = None, body: list[stmt] = ..., *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.type = type
        self.name = name
        self.body = body if (body is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class arguments(AST):
    __match_args__ = ('posonlyargs', 'args', 'vararg', 'kwonlyargs', 'kw_defaults', 'kwarg', 'defaults')
    _fields = ('posonlyargs', 'args', 'vararg', 'kwonlyargs', 'kw_defaults', 'kwarg', 'defaults')

    def __init__(self, posonlyargs: list[arg] = ..., args: list[arg] = ..., vararg: Optional[arg] = None, kwonlyargs: list[arg] = ..., kw_defaults: list[expr] = ..., kwarg: Optional[arg] = None, defaults: list[expr] = ...) -> None:
        self.posonlyargs = posonlyargs if (posonlyargs is not ...) else []
        self.args = args if (args is not ...) else []
        self.vararg = vararg
        self.kwonlyargs = kwonlyargs if (kwonlyargs is not ...) else []
        self.kw_defaults = kw_defaults if (kw_defaults is not ...) else []
        self.kwarg = kwarg
        self.defaults = defaults if (defaults is not ...) else []

class arg(AST):
    __match_args__ = ('arg', 'annotation', 'type_comment')
    _fields = ('arg', 'annotation', 'type_comment')

    def __init__(self, arg: str, annotation: Optional[expr] = None, type_comment: Optional[str] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.arg = arg
        self.annotation = annotation
        self.type_comment = type_comment
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class keyword(AST):
    __match_args__ = ('arg', 'value')
    _fields = ('arg', 'value')

    def __init__(self, arg: Optional[str] = None, value: expr, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.arg = arg
        self.value = value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class alias(AST):
    __match_args__ = ('name', 'asname')
    _fields = ('name', 'asname')

    def __init__(self, name: str, asname: Optional[str] = None, *, lineno: int, col_offset: int, end_lineno: Optional[int] = None, end_col_offset: Optional[int] = None) -> None:
        self.name = name
        self.asname = asname
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class withitem(AST):
    __match_args__ = ('context_expr', 'optional_vars')
    _fields = ('context_expr', 'optional_vars')

    def __init__(self, context_expr: expr, optional_vars: Optional[expr] = None) -> None:
        self.context_expr = context_expr
        self.optional_vars = optional_vars

class match_case(AST):
    __match_args__ = ('pattern', 'guard', 'body')
    _fields = ('pattern', 'guard', 'body')

    def __init__(self, pattern: pattern, guard: Optional[expr] = None, body: list[stmt] = ...) -> None:
        self.pattern = pattern
        self.guard = guard
        self.body = body if (body is not ...) else []

class pattern(AST):
    __match_args__ = ()
    _fields = ()

    def __init__(self, *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class MatchValue(pattern):
    __match_args__ = ('value')
    _fields = ('value')

    def __init__(self, value: expr, *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.value = value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class MatchSingleton(pattern):
    __match_args__ = ('value')
    _fields = ('value')

    def __init__(self, value: object, *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.value = value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class MatchSequence(pattern):
    __match_args__ = ('patterns')
    _fields = ('patterns')

    def __init__(self, patterns: list[pattern] = ..., *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.patterns = patterns if (patterns is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class MatchMapping(pattern):
    __match_args__ = ('keys', 'patterns', 'rest')
    _fields = ('keys', 'patterns', 'rest')

    def __init__(self, keys: list[expr] = ..., patterns: list[pattern] = ..., rest: Optional[str] = None, *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.keys = keys if (keys is not ...) else []
        self.patterns = patterns if (patterns is not ...) else []
        self.rest = rest
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class MatchClass(pattern):
    __match_args__ = ('cls', 'patterns', 'kwd_attrs', 'kwd_patterns')
    _fields = ('cls', 'patterns', 'kwd_attrs', 'kwd_patterns')

    def __init__(self, cls: expr, patterns: list[pattern] = ..., kwd_attrs: list[str] = ..., kwd_patterns: list[pattern] = ..., *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.cls = cls
        self.patterns = patterns if (patterns is not ...) else []
        self.kwd_attrs = kwd_attrs if (kwd_attrs is not ...) else []
        self.kwd_patterns = kwd_patterns if (kwd_patterns is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class MatchStar(pattern):
    __match_args__ = ('name')
    _fields = ('name')

    def __init__(self, name: Optional[str] = None, *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.name = name
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class MatchAs(pattern):
    __match_args__ = ('pattern', 'name')
    _fields = ('pattern', 'name')

    def __init__(self, pattern: Optional[pattern] = None, name: Optional[str] = None, *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.pattern = pattern
        self.name = name
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class MatchOr(pattern):
    __match_args__ = ('patterns')
    _fields = ('patterns')

    def __init__(self, patterns: list[pattern] = ..., *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.patterns = patterns if (patterns is not ...) else []
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class type_ignore(AST):
    __match_args__ = ()
    _fields = ()


class TypeIgnore(type_ignore):
    __match_args__ = ('lineno', 'tag')
    _fields = ('lineno', 'tag')

    def __init__(self, lineno: int, tag: str) -> None:
        self.lineno = lineno
        self.tag = tag

class type_param(AST):
    __match_args__ = ()
    _fields = ()

    def __init__(self, *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class TypeVar(type_param):
    __match_args__ = ('name', 'bound', 'default_value')
    _fields = ('name', 'bound', 'default_value')

    def __init__(self, name: str, bound: Optional[expr] = None, default_value: Optional[expr] = None, *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.name = name
        self.bound = bound
        self.default_value = default_value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class ParamSpec(type_param):
    __match_args__ = ('name', 'default_value')
    _fields = ('name', 'default_value')

    def __init__(self, name: str, default_value: Optional[expr] = None, *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.name = name
        self.default_value = default_value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

class TypeVarTuple(type_param):
    __match_args__ = ('name', 'default_value')
    _fields = ('name', 'default_value')

    def __init__(self, name: str, default_value: Optional[expr] = None, *, lineno: int, col_offset: int, end_lineno: int, end_col_offset: int) -> None:
        self.name = name
        self.default_value = default_value
        self.lineno = lineno
        self.col_offset = col_offset
        self.end_lineno = end_lineno
        self.end_col_offset = end_col_offset

