#include"rb_cuda.h"
#include<stdio.h>
#include<stdlib.h>


int main(int argc, char* argv[]){
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <n> <iters>\n", argv[0]);
        return 1;
    }
    calculate(atoi(argv[1]), atoi(argv[2]));
    return 0;
}