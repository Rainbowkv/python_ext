// #include<cuda_runtime.h>
#include"rb_cuda.h"

__global__ void _calculate(float* d_a, float* d_b, float* d_c, int n, int iters){
    int idx = blockDim.x * blockIdx.x + threadIdx.x;
    if(idx == 7){
        printf("Hello from cuda_0: thread_7 .\n");
    }
    if(idx < n){
        for(int i=0;i<iters;i++)
            d_c[idx] += d_a[idx] + d_b[idx];
    }
    return;
}

void calculate(int n_power, int iters_power){
    int n = 1 << n_power;
    int iters = 1 << iters_power;
    printf("rb_cuda校验 -> n: %d, iters: %d\n", n, iters);
    int block_size = 256;
    int grid_size = ceil(n/block_size);
    int size = n*sizeof(float);
    float* h_a = (float*)malloc(size);
    float* h_b = (float*)malloc(size);
    float* h_c = (float*)malloc(size);

    for(int i=0;i<n;i++){
        h_a[i] = i;
        h_b[i] = i;
    }

    float* d_a, *d_b, *d_c;
    cudaMalloc((void **)&d_a, size);
    cudaMalloc((void **)&d_b, size);
    cudaMalloc((void **)&d_c, size);
    cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);

    std::cout << "Correspond cpu_thread is blocked...\n" << std::endl;

    _calculate<<<grid_size, block_size>>>(d_a, d_b, d_c, n, iters);

    // 检查内核执行错误
    // CUDA_CHECK(cudaGetLastError());
    cudaDeviceSynchronize();
    cudaMemcpy(h_c, d_c, n, cudaMemcpyDeviceToHost);

    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    for(int i=0;i<1<<4;i++){
        printf("%f + %f = %f\n", h_a[i], h_b[i], h_c[i]);
    }
    
    free(h_a);
    free(h_b);
    free(h_c);

    std::cout << "Correspond cpu_thread is running...\n" << std::endl;
    return;
}