#include <stdio.h>

void main(){
    float n;
    float soma = 0;
    float cont = 1;

    scanf("%f", &n);
    while (n >= 0 ){
        soma += n;
        cont ++;
        scanf("%f", &n);
    }

    printf("%.2f\n", soma / (cont - 1));


}

