#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int busca_binaria(int vet[], int chave, int Tam)
{
     int inf = 0;     // limite inferior (o primeiro índice de vetor em C é zero          )
     int sup = Tam-1; // limite superior (termina em um número a menos. 0 a 9 são 10 números)
     int meio;
     
     while (inf <= sup)
     {
          meio = (inf + sup)/2;
          if (chave == vet[meio])
		  {
		  	int i = meio;
		  	while(vet[i] == chave)
		  		meio = i--;
		  	return meio;
		  }
          if (chave < vet[meio])
               sup = meio-1;
          else
               inf = meio+1;
     }
     return -1;   // não encontrado
}

int main(){
	int x = 1, y = 1;
	int cont = 0;
	cin >> x >> y;
	
	while(cont < 66 && x != 0 && x != 0){
		
		cout << "CASE# " << ++cont << ":" << endl; 
		
		int vetor[x];
		for(int i = 0; i < x; i++)
		{
			int e;
			cin >> e;
			
			vetor[i] = e;
		}
		
		sort(vetor, vetor + x);
		
		
		for(int i = 0; i < y; i++)
		{
			
			int e, achou = -1; 
			cin >> e;
			
			achou = busca_binaria(vetor, e, x);
			if(achou != -1)
				cout << e << " found at " << achou + 1 << endl;
			else
				cout << e << " not found" << endl;
		}
		
		cin >> x >> y;
	}
	return 0;
}
