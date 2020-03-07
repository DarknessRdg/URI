/**
 * Refazendo a questao em C++ pra mostrar pro lucas que da pra fazer
 * ela sem usar uma pilha e que ele consegue fazer sim kkkk!
 * 
 * Forte abraço ! hahaha
 */
#include <iostream> 
using namespace std; 

class Carro {
public:
   	   int entrada;
   	   int saida;
   
   Carro(int e, int s) {
	   entrada = e;
	   saida = s;
   }	
};


void add_carro(Carro* carro, Carro* vetor[], int posicao) {
	vetor[posicao] = carro;
}


bool programa(int motoristas, int qnt_vagas) {
	Carro* carros[motoristas];
	
	for (int i = 0; i < motoristas; i++) {
		int entrada, saida;
		cin >> entrada;
		cin >> saida;
		carros[i] = new Carro(entrada, saida);
	}
	
	Carro* estacionamento[qnt_vagas];
	int qnt_no_estacionamento = 0;
	for (int i = 0; i < motoristas; i++) {
		Carro* carro = carros[i];

		if (qnt_no_estacionamento == 0) {  // estacionamento vazio
			add_carro(carro, estacionamento, qnt_no_estacionamento);
			qnt_no_estacionamento++;
			continue;
		}
		
		Carro* ultimo = estacionamento[qnt_no_estacionamento - 1];

		if (carro->entrada >= ultimo->saida) { // entra dps da saida do ultimo
		// ou no msm tempo
		
			qnt_no_estacionamento --;
			i --; // continua no msm morotista
		}
		else if (carro->saida <= ultimo->saida) { // sai antes do ultimo ou ao
        // mesmo tempo
			add_carro(carro, estacionamento, qnt_no_estacionamento++);
		}
		else if (carro->entrada > ultimo->saida) {  // entra dps que ultimo sai
			qnt_no_estacionamento --;
			i --; // continua no msm morotista			
		}
		else return false;
		
		if (qnt_no_estacionamento > qnt_vagas) // passou do limite de carros no estacionamento
			return false;
	}

	for (int i = 0; i < qnt_no_estacionamento - 1; i++) {
		// cout << estacionamento[i]->saida << " " << estacionamento[i+1]->saida << endl;
		if (estacionamento[i]->saida < estacionamento[i+1]->saida)
			return false;
	}
	
	return true;
}

int main() {
	int n = 1, k = 1;
	
	cin >> n;
	cin >> k;
	
	while (n != 0 && k != 0) {
		if (programa(n, k))
			cout << "Sim";
		else
			cout << "Nao";
		cout << endl;
		
		cin >> n;
		cin >> k;
	}
	return 0;
}
