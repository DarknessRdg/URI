#include <stdio.h>

void main(){
    int n;
    scanf("%d", &n);

    int i;
    for (i = 1; i <= n; i ++){
        if (n % i == 0){
            printf("%d\n", i);
        }
    }
}

