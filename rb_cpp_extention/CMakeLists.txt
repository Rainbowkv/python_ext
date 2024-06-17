cmake_minimum_required(VERSION 3.12)

project(RBMath)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(LIBRARY_NAME rb_math)
add_library(${LIBRARY_NAME} SHARED rb_math.cpp)

set_target_properties(${LIBRARY_NAME} PROPERTIES OUTPUT_NAME "rb_math")

target_include_directories(${LIBRARY_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

