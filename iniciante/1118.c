#include <stdio.h>

void calculo();
void main(){
    int op = 1;
    while (op != 2){
        calculo();
        while (1){
            printf("novo calculo (1-sim 2-nao)\n");
            scanf("%d", &op);
            if (op == 1 || op == 2){
                break;
            }
        }
    }
}

void calculo(){
    float n, soma;
    int qnt = 0;
    while (qnt != 2){
        scanf("%f", &n);
        if (n >= 0 && n <= 10){
            soma += n;
            qnt ++;
        }else{
            printf("nota invalida\n");
        }
    }

    printf("media = %.2f\n", soma / 2);
}
