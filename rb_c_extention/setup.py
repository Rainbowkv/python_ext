from setuptools import setup, Extension


module = Extension("rainbow_c.math", sources = ["math.c"])

setup(
    name="rainbow_c",
    version="0.0.1",
    description="C_extention of rb",
    packages=["rainbow_c", "rainbow_c.math"],
    package_dir={"rainbow_c": "rainbow", "rainbow_c.math": "rainbow/math"},
    ext_modules=[module]
)
