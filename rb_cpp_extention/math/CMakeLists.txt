cmake_minimum_required(VERSION 3.12)

project(math)

set(CMAKE_CXX_STANDARD 14)

find_package(pybind11 REQUIRED)

add_library(math MODULE math.cpp add.cpp sub.cpp)

# 设置pyd的导出目录
set_target_properties(math PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/rainbow)

target_link_libraries(math PRIVATE pybind11::module)