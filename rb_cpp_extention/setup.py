from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext


include_path = "include/"
dll_path = "build/Release/"
ext_modules = [
    Pybind11Extension(
        "rainbow.math",  # 这将生成rainbow/math.pyd的文件
        # ["math/math.cpp", "math/add.cpp", "math/sub.cpp"],
        ["math/math_dll.cpp"],
        include_dirs=[include_path],
        library_dirs=[dll_path],
        libraries=["rb_math"],
    )
]  # 1. 简单的项目就可以这样构造

setup(
    name="rainbow",
    version="0.0.1",
    author="rainbow",
    author_email="rainbowkv@163.com",
    description="A C++ extension package made by rainbow",
    packages=["rainbow", "rainbow.math", "rainbow.lib"],
    package_dir={"rainbow": ".", "rainbow.math": "math", "rainbow.lib": "lib"},  # 前者是包名，后者是包名指定的目录。即告诉setuptools哪个目录就是这个包。这样math才不会在site-packages下与rainbow同级，而是在rainbow目录下
    package_data={"rainbow.lib": ["*.dll"]},  # 指定不想被过滤的非python的文件
    ext_modules=ext_modules,  # 1. 简单的项目就可以这样构造
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C++",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)