#include <pybind11/pybind11.h>
#include "C:/D/program_dev/cpp_project/include/math.h"


PYBIND11_MODULE(math, m) {
    m.def("add", &add, "Calculate the sum of two numbers, maybe overflow.");
    m.def("sub", &sub, "Calculate the dif of two numbers, maybe overflow.");
}