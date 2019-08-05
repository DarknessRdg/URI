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
	
	void show(){
		No* aux;
		aux = inicio;
		if(!vazia())
		{
			cout << aux->valor << " "; aux = aux->prox;
			while(aux != inicio){cout << aux->valor << " "; aux = aux->prox;}
				cout << endl;
		}
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
		free(posicao);
		length --;
	}
	
};


int main(){	
	int x;
	cin >> x;
	for(int i = 0; i < x; i++)
	{
		Circulo* c = new Circulo();
		int qnt, salto;
		cin >> qnt >> salto;
		for(int j = 1; j <= qnt; j++){c->insere(j);}
			
        while(c->length != 1){c->mudaInicio(salto);}
		
		cout << "Case " << i + 1 << ": " << c->inicio->valor << endl; 		
	}
 	

	return 0;
}
