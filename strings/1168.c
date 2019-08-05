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
    char n[100000];
    int x;
    scanf("%d%*c", &x);
        for(; x > 0; x--)
        {
            int j, cont = 0;
            gets(n);
            for(j = 0; j < len(n); j ++)
            {
                switch(n[j])
                {
                    case '1':
                        cont += 2;
                        break;
                    case '2':
                        cont += 5;
                        break;
                    case '3':
                        cont += 5;
                        break;
                    case '4':
                        cont += 4;
                        break;
                    case '5':
                        cont += 5;
                        break;
                    case '6':
                        cont += 6;
                        break;
                    case '7':
                        cont += 3;
                        break;
                    case '8':
                        cont += 7;
                        break;
                    case '9':
                        cont += 6;
                        break;
                    case '0':
                        cont += 6;
                        break;
                } // switch
            } // for j
            printf("%d leds\n", cont);
        } // fim programa
return 0;
}
