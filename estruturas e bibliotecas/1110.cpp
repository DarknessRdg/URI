#include <iostream>
using namespace std;

class No{
	public:
		int valor;
		No* prox;
		No* ant;

		No(int valor){
			this->valor = valor;
			this->prox = NULL;
			this->ant = NULL;
		}
};

class Fila{
	public:
		No* inicio;
		No* fim;
		int len;
	
	Fila(int qnt){
		len = 0;
		inicio = fim = NULL;
		this->init(qnt);
	}
	
	void init(int qnt){
		for(int i = 1; i <= qnt; i++)
			this->push(i);
	}
	
	
	void push(int valor){
		len ++;
		
		No* n = new No(valor);
		if(this->vazia())
			inicio = fim = n;
		else{
			fim->prox = n;
			fim = n;
		}
	}
	
	bool vazia(){ return inicio == NULL;}
	
	
	No* pop(){
		len --;
		No* aux = inicio;
		inicio = inicio->prox;
		return aux;
	}
	
	int last(){
		return inicio->valor;
	}
	
	void show(){
		if(this->vazia())
			return;
		
		No* aux = inicio;
		cout << aux->valor << " ";
		
		while(aux->prox){
			aux = aux->prox;
			cout << aux->valor << " ";
		}
	}
};
	

int main(){
	int qnt;
	cin >> qnt;
	while(qnt != 0){
	   	Fila* f = new Fila(qnt);
	   	
	    cout << "Discarded cards:" ; 
	   	
		while(f->len >= 2){
			cout << " " << f->pop()->valor;

		if(f->len >= 2)
				cout << ",";
			
			f->push(f->pop()->valor);	   
		}
		cout << endl;
		cout << "Remaining card: " << f->pop()->valor << endl;
	   	
		
		
		cin >> qnt;	   
	}
	return 0;
}
