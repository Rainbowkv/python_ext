#ifndef RB_MATH_H
#define RB_MATH_H

#include<stdio.h>

#ifndef DDL_IMPORT
#define API __declspec(dllexport)
#else
#define API __declspec(dllimport)
#endif

extern "C"{  // 必须写在这个声明，
             // 否则编译cpp源文件的CPP编译器找到此头文件后会对函数名进行修饰。外面就找不到原始的add。
    API void add();
    API void sub();
}

#endif