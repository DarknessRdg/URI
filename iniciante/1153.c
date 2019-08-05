#include <stdio.h>

int fat();


void main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", fat(n));
}

int fat(n){
    if (n == 0){
        return 1;
    }else{
        return n * fat(n - 1);
    }


}
