#include <stdio.h>

void main(){
    float soma = 0;

    int i;

    for (i = 1; i < 101; i ++){
        soma += (1.0 / i);
    }
    printf("%.2f\n", soma);

}

