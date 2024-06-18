import rainbow_cuda.tensor_add


print(rainbow_cuda.tensor_add)
rainbow_cuda.tensor_add.calculate(20, 20)

# import ctypes

# tensor_add = ctypes.CDLL("./rb_cuda.dll")
# tensor_add.calculate.argtypes = [ctypes.c_int, ctypes.c_int]
# tensor_add.calculate.restype = None

# tensor_add.calculate(20, 10)