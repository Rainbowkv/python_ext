cmake_minimum_required(VERSION 3.12)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

project(RBMath LANGUAGES CXX)

add_executable(
    test_rb_cuda
    test_rb_cuda.cpp 
)

target_include_directories(test_rb_cuda PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../rb_cuda_extention/include)

target_link_libraries(test_rb_cuda "${CMAKE_CURRENT_SOURCE_DIR}/../rb_cuda_extention/build/Release/rb_cuda.lib")