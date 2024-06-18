cmake_minimum_required(VERSION 3.23)

set(CMAKE_CUDA_ARCHITECTURES "60;61;62;70;72;75;80;86;89")

set(CMAKE_CXX_STANDARD 17)

# cmake_policy(SET CMP0144 NEW)

project(RBCUDA LANGUAGES CXX CUDA)

find_package(CUDAToolkit REQUIRED)

file(GLOB SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/*.c* ${CMAKE_CURRENT_SOURCE_DIR}/*.h)

add_executable(
    rb_cuda ${SOURCE_DIR}
)

target_link_libraries(rb_cuda PUBLIC CUDA::cudart)
