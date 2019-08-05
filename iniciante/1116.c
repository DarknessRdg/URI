#include <stdio.h>

void main(){
    int n;
    scanf("%d", &n);
    int i;

    for (i = 0; i < n; i++){
        int a, b;
        scanf("%d %d", &a, &b);
        if (b == 0){
            printf("divisao impossivel\n");
        }else{
            printf("%.1f\n", (float) a / b);
            }
    }
}
