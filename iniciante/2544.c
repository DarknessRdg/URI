#include <stdio.h>
#include <math.h> 


int main(){
	int x;
	while(scanf("%d", &x) == 1){
		if(x <= 2)
			printf("%d\n", x / 2);
		else
		  		printf("%.0f\n",  log10(x) / log10(2) );
	}
	return 0;
}