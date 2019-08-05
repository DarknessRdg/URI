#include <stdio.h>

int main()
{
    
    float sum = 0;

    char operacao;
    int fim = 11;
    scanf("%c", &operacao);
    int i, j;
    for ( i  = 0; i < 12; i++)
    {
        for ( j = 0; j < 12; j++)
        {
            float entrada;
            scanf("%f", &entrada);
            if (j < fim)
                sum += entrada;
        }
        fim --;

    }

    switch (operacao)
    {
    case 'S':
        printf("%.2f\n", sum);
        break;
    
    default:
        printf("%.1f\n", sum / 66);
        break;
    }

    return 0;
}