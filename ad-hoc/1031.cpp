#include <iostream>
#include <stdlib.h>

using namespace std;

class No{
	public:
		int valor;
		No* prox;
		
		No(int x, No* z)
		{
			valor = x;
			prox = z;
		}	
};

class Circulo{
	public:
	No* inicio;
	No* fim;
	int length;
	
	Circulo(){ inicio = NULL; fim = NULL; length = 0;}
	
	bool vazia(){return inicio == NULL;}
	
	void insere(int valor)
	{
		if(vazia()){
			inicio = new No(valor, NULL);
			fim = inicio; 
		}
		else{
			No* novo = new No(valor, inicio);
			fim->prox = novo;
			fim = novo;
		}
		length ++;
	}	

	
	void mudaInicio(int posi){
		No* posicao; No* aux; No* ant;
		ant = fim;
		aux = inicio;
		for(int i = 1; i <= posi; i++){
			if(i == posi - 1) ant = aux;
			posicao = aux;
			aux = aux->prox;
		}
		
		ant->prox = posicao->prox;		
		inicio = posicao->prox;
		fim = ant;
		length --;
	}
	
};


int main(){	
	int i;
	cin >> i;
	while(i != 0){
		int qnt, salto = 1;
		qnt = i;
		
		while(1){
			Circulo* c = new Circulo();
			
			for(int j = 2; j <= qnt; j++){c->insere(j);}
				
		    while(c->length != 1){c->mudaInicio(salto);}
			
			if(c->inicio->valor == 13){
				cout << salto << endl;
				break;
			}
			else{ salto ++; }
			 		
		}
		cin >> i;
	}
	return 0;
}
