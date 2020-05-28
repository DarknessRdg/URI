#include <stdio.h>

int tamanho(char *lista);
int eh_letra(char letra);
void inverte(char *palavra, int tam);

int main()
{
    int qnt;
    scanf("%d%*c", &qnt);
    int  i = 0;
    for (; i < qnt; i ++)
    {
        char palavra[1000];
        gets(palavra);
        int j = 0;
        int tam = tamanho(palavra);
        /* primeira */
        for (j = 0; j < tam; j++)
        {
            if(eh_letra(palavra[j]))
            {
                palavra[j] = palavra[j] + 3;
            }
        }

        /* Segunda */
        inverte(&palavra, tam);

        /* Tercira */
        int metade = tam / 2;
        for (j = metade; j < tam; j++)
            palavra[j] --;

        printf("%s\n", palavra);

    }

return 0;
}

void inverte(char *palavra, int tam)
{
    char aux;
    int i, metade = tam / 2;
    tam --;
    for (i = 0; i < metade; i ++)
    {
        aux = palavra[i];
        palavra[i] = palavra[tam];
        palavra[tam] = aux;
        tam --;
    }
}

int eh_letra(char letra)
{
    if (((letra <= 'z') && (letra >= 'a')) || (letra <= 'Z') && (letra >= 'A'))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int tamanho(char *lista)
{
    int cont = 0;
    while (*lista ++){
        cont ++;
    }
    return cont;
}
