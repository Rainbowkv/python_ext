import ctypes


rb_math = ctypes.CDLL("build/Release/rb_math.dll")
rb_math.add()
