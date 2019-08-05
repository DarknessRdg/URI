#include <stdio.h>

void main(){
    float soma = 1.0;

    int baixo = 2;
    int i;
    for (i = 3; i < 40; i += 2){
        soma += ((float)i / baixo);
        baixo = baixo * 2;
    }
    printf("%.2f\n", soma);

}

