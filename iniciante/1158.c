#include <stdio.h>

void main(){
    int n;
    scanf("%d", &n);

    int i;
    for (i = 0; i < n; i ++){

        int x, y, cont = 0, soma = 0;

        scanf("%d %d", &x, &y);

        while (cont < y){
            if (x % 2 != 0){
                soma += x;
                cont ++;
            }
            x ++;
        }

        printf("%d\n", soma);
    }


}
