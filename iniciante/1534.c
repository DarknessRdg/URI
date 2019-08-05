#include <stdio.h>

void imprime(int* v, int j)
{
	int i;
	for(i = 0; i < j; i++)
		printf("%d" , v[i]);
	printf("\n");
}

void altera(int* v, int vez1, int vez2)
{
	v[vez1] = 1;
	v[vez2] = 2;	
}

void voltaNormal(int* v, int vez1, int vez2)
{
	v[vez1] = 3;
	v[vez2] = 3;
}

int main()
{
	while(1)
	{
		
		int qnt;
		scanf("%d", &qnt);

		if(feof(stdin)) 
			break;
			
		int sequencia[90];
		
		int i;
		for(i = 0; i < qnt; i++)
			sequencia[i] = 3;
		
		
		int vez1 = 0;
		int vez2 = qnt - 1;
		for(i = 0; i < qnt; i++)
		{
			altera(sequencia, vez1, vez2);
			imprime(sequencia, qnt);
			voltaNormal(sequencia, vez1, vez2);
			vez1 ++;
			vez2 --;	
			
		}
		
	}
	
	
	return 0;
}