#include<cuda_runtime.h>
#include<iostream>

__global__ void hello(){
    printf("Hello from cuda_0.\n");
    return;
}

int main(){
    std::cout << "Hello from cpu." << std::endl;
    hello<<<1,1>>>();
    cudaDeviceSynchronize();
    return 0;
}