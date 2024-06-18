#include <pybind11/pybind11.h>
#include "rb_cuda.h"


void calculate_wrapper(pybind11::object n_obj, pybind11::object iters_obj) {
    // 从 Python 对象转换为 C++ 整数
    int n = n_obj.cast<int>();
    int iters = iters_obj.cast<int>();
    printf("tensor_add.cpp校验 -> n_power: %d, iters_power: %d\n", n, iters);
    // 调用实际的 calculate 函数
    calculate(n, iters);
}

PYBIND11_MODULE(tensor_add, m) {
    m.def("calculate", &calculate_wrapper, "Calculate the sum of two vectors repeated specified times.");
}