#include <stdio.h>

int len(char *n)
{
    int cont = 0;
    while(*n++)
        cont ++;
    return cont;
}

void lower(char *n, int tam)
{
    int i;
    for(i = 0; i < tam; i++)
    {
        if((n[i] >= 'A') && (n[i] <= 'Z'))
            n[i] = n[i] + ('a' - 'A');
    }
}

int main()
{

    while(1)
    {
        char entrada[5000];
        gets(entrada);
        if (feof(stdin))
            break;
        else{
        int tam = len(entrada);
        lower(&entrada, tam);


        int i, espaco = 0;
        int cont1 = 0, cont2 = 0;

        for (i = 0; i < tam; i++)
        {
            if (entrada[i] == ' ')
            {
                if (entrada[i + 1] == entrada[espaco])
                {
                    if(cont2 == 0)
                    {
                        cont1 ++;
                        cont2 ++;
                    }
                }else{ cont2 = 0 ;}

                espaco = i + 1;
            }


        }
        printf("%d\n", cont1);
        }
    }
return 0;
}
