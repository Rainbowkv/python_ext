cmake_minimum_required(VERSION 3.23)

# 设置CUDA架构
set(CMAKE_CUDA_ARCHITECTURES "60;61;62;70;72;75;80;86;89")

# 设置C++标准
set(CMAKE_CXX_STANDARD 17)

# cmake_policy(SET CMP0144 NEW)

# 设置项目名称和使用的语言
project(RBCUDA LANGUAGES CXX CUDA)

# 包含头文件目录
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# 查找CUDA工具包
find_package(CUDAToolkit REQUIRED)

# 查找源文件，生成源文件列表
file(GLOB SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/*.c* ${CMAKE_CURRENT_SOURCE_DIR}/*.h)

# 添加共享库
add_library(rb_cuda SHARED ${SOURCE_DIR})

# 链接CUDA运行时库
target_link_libraries(rb_cuda PUBLIC CUDA::cudart)
