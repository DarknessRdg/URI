#include <stdio.h>

void fib();


void main(){
    int n;
    scanf("%d", &n);
    fib(n);
    printf("\n");
}

void fib(n){
    int vetores[n];

    int i;
    for(i = 0; i < n; i ++){
        if (i == 0){
            vetores[i] = 0;
            printf("%d", vetores[i]);
        }else if (i == 1){
            vetores[i] = 1;
            printf(" %d", vetores[i]);
        }else{
            vetores[i] = vetores[i - 1] + vetores[i - 2];
            printf(" %d", vetores[i]);
        }
    }
}
