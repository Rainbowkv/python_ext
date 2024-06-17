#include <pybind11/pybind11.h>

int add(int a, int b);
int sub(int a, int b);

PYBIND11_MODULE(math, m) {
    m.def("add", &add, "Calculate the sum of two numbers, maybe overflow.");
    m.def("sub", &sub, "Calculate the dif of two numbers, maybe overflow.");
}