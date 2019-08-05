#include <stdio.h>

int main()
{
	int qnt, i, a, b;
	scanf("%d", &qnt);
	
	for(i = 0; i < qnt; i++)
	{
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
	}
		
	return 0;
}


