#include <stdio.h>

void main(){

    float soma = 0;
    int qnt = 0;

    while(qnt != 2){
        float a;
        scanf("%f", &a);
        if ((a >= 0) && (a <= 10)){
            soma += a;
            qnt += 1;
        }else{
            printf("nota invalida\n");
        }

    }
    printf("media = %.2f\n", soma / 2);
}

