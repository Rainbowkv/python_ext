#include<iostream>

#ifndef DDL_IMPORT
#define API __declspec(dllexport)
#else
#define API __declspec(dllimport)
#endif

extern "C"{
    API void calculate(int n_power, int iters_power);
}