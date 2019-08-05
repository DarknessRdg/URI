#include <stdio.h>
#include <math.h>

int main()
{
	char entrada[100];
	int a, b, c;
	
	fgets(entrada, 100, stdin);
	while(entrada[0] != '0')
	{
		sscanf(entrada, "%d %d %d", &a, &b, &c);
		float resultado = sqrt((a * b * 100) / c);
		printf("%.0f\n", trunc(resultado));
		fgets(entrada, 100, stdin);
	}	
		
	return 0;
}


