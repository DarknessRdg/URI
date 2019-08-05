#include <stdio.h>

void main(){
    while(1){
        int a, b;
        scanf("%d %d", &a, &b);

        if (a > b){
            printf("Decrescente\n");
        }else if (a == b){
            break;
        }else{
            printf("Crescente\n");
        }

    }

}
