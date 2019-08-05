#include <stdio.h> 

int main(){
	
	int j;
	scanf("%d", &j);
	
	int i;	
	for(i = 1; i <= j; i++)
	{
		printf("%d %d %d\n", i, i*i, i*i*i);
	}
	return 0;
}