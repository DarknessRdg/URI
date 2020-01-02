#include <stdio.h>


void swap(int* a, int* b) {
    int aux = *a;
    *a = *b;
    *b = aux;
}


int sort(int v[], int tam) {
    int cont = 0;

    int i;
    for(i = 0; i < tam; ) {
        if (v[i] == i + 1) {
            i ++;
            continue;
        }
        
        cont ++;
        swap(&v[i], &v[v[i]-1]);

        i = 0;
    }

    return cont;
}



int main() {

    int n;
    scanf("%d", &n);

    int i, j, number;
    for (i = 0; i < n; i++) {
        scanf("%d", &number);
        int v[number];

        for (j = 0; j < number; j++)
            scanf("%d", &v[j]);
        
        printf("%d\n", sort(v, number));
    }

    return 0;
}