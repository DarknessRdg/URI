#include <stdio.h> 

int main(){
	
	int j;
	scanf("%d", &j);
	
	int i;
	for(i = 0;  i < j; i++)
	{
		int x,y;
		scanf("%d %d", &x, &y);
		int r = (3 * x) * (3 * x) + (y * y);
		int b = (2 * x * x) + (5 * y) * (5 * y);
		int c = y * y * y - (100 * x);
		
		if (r > b && r > c)
			printf("Rafael ganhou\n");
		else if (b > r && b > c)
			printf("Beto ganhou\n");
		else 
			printf("Carlos ganhou\n");
	}
	return 0;
}
