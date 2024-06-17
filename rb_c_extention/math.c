// #include <C:\Users\rainbow\anaconda3\envs\rainbow_GPT\include\python.h>
#include <python.h>
#include <stdio.h>

static PyObject* add(PyObject* self, PyObject* args){
    long long a;
    long long b;
    if(!PyArg_ParseTuple(args, "LL", &a, &b)){
        return NULL;
    }
    return Py_BuildValue("L", a + b);
}

static PyObject* sub(PyObject* self, PyObject* args){
    long long a;
    long long b;
    if(!PyArg_ParseTuple(args, "LL", &a, &b)){
        return NULL;
    }
    return Py_BuildValue("L", a - b);
}

static PyMethodDef methods[] = {
    {"add", add, METH_VARARGS, "Calculate the sum of two numbers, maybe overflow."},
    {"sub", sub, METH_VARARGS, "Calculate the dif of two numbers, maybe overflow."},
    {NULL, NULL, 0, NULL}
};

static PyModuleDef math = {
    PyModuleDef_HEAD_INIT,
    "math",
    "A math module of c_extention of rb",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_math(){
    return PyModule_Create(&math);
}
