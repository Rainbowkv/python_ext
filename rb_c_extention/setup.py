from setuptools import setup, Extension


module = Extension("math", sources = ["math.c"])

setup(
    name="math",
    version="0.0.1",
    description="A math module of c_extention of rb",
    ext_modules=[module]
)
