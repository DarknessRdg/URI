#include <iostream>
#include <math.h>
using namespace std;

void print(int n){
	string espacos;
	if(n < 10)
		espacos = "   ";
	else if(n < 100)
		espacos = "  ";
	else
		espacos = " ";
	
	cout << espacos << n ;
}

int main(){
	int n; cin >> n;
	while(n != 0)
	{
		
		for(int i = 1; i <= n; i++)
		{
			int cont = i;
			bool decrement = true;
			
			if(cont < 10)
				cout << "  " << cont;
			else if(cont < 100)
				cout << " " << cont;
			else
				cout << cont;
			
			for(int j = 1; j < n; j++)
			{
				if(cont == 1)
					decrement= false;
				if(decrement)
					cont --;
				else 
					cont ++;
				print(cont);
			}
			cout << endl;
		}
		
		cout << endl;
		cin >> n;
	}
	return 0;
}	