import os

__all__ = [
    "calculate"
]


dll_path = os.path.join(os.path.dirname(__file__), "lib")
os.add_dll_directory(dll_path)

from rainbow_cuda.tensor_add import calculate
