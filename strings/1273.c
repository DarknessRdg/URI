#include <stdio.h>

int len(char *n)
{
    int cont = 0;
    while(*n++)
        cont ++;
    return cont;
}

int main()
{
    int op, cont = 1;
    scanf("%d%*c", &op);
    while(op)
    {
        if (cont != 1)
            printf("\n");
        char p[op][50];

        int i, maior = 0;
        for(i = 0; i < op; i++)
        {
            scanf("%s", p[i]);

            int tam = len(p[i]);
            if (tam > maior)
                maior = tam;
        }
        int j;
        for (i = 0; i < op; i++)
        {
            for(j = 0; j < (maior - len(p[i])); j++){
                printf(" ");
            }
            printf("%s\n", p[i]);
        }
        scanf("%d%*c", &op);
        cont ++;
    }

return 0;
}
