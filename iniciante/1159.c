#include <stdio.h>


void main(){
    int x;
    scanf("%d", &x);
    while (x){

        int soma = 0, qnt = 0;

        int aux;
        aux = x;
        while(qnt < 5){
           if (x % 2 == 0){
                soma += x;
                qnt ++;
           }
           x ++;
        }
        printf("%d\n", soma);
        scanf("%d", &x);
    }
}
