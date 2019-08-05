#include <stdio.h>

void main(){
    int x, y, maior, menor;

    scanf("%d", &x);
    scanf("%d", &y);

    if (y > x){
        maior = y;
        menor = x;
    }else{
        maior = x;
        menor = y;
    }
    int i;
    for (i = menor + 1; i < maior; i++){
        if ((i % 5 == 2) || (i % 5 == 3))
            printf("%d\n", i);
    }


}
