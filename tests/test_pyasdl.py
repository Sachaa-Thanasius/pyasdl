import pathlib
import time

import pyasdl


class TimeCatcher:
    def __enter__(self):
        self.elapsed = time.perf_counter()
        return self

    def __exit__(self, *_exc_info: object):
        self.elapsed = time.perf_counter() - self.elapsed


source_dir = pathlib.Path("tests")
source = source_dir.joinpath("Python.asdl").read_text("utf-8")

with TimeCatcher() as tc:
    code = pyasdl.generate_code(source)

source_dir.joinpath("Python_asdl.py").write_text(code, "utf-8")

print(f"Time taken: {tc.elapsed}")
