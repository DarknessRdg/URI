#include <iostream>
#define optimize ios::sync_with_stdio(false);cin.tie(NULL)
#define MAX 100010 
using namespace std;


long long  TOTAL_ATUAL;

long long soma_string(string nome) {
	long long soma = 0, i = 0;
	while (nome[i])
		soma += nome[i++];
	return soma;
}


/**
 * Somas todos do inicio até o elemento sorteado
 * (incluido o sorteado)
 */
long long  soma_esquerda(long long  sorteado, long long  JOGADORES[]) {
	long long  peso = 1;
	long long  soma = 0;
	
	for (long long  posicao = sorteado; posicao >= 0; posicao--) {
		soma += JOGADORES[posicao] * peso;	
		peso ++;
	}
	return soma;
}

/**
 * Soma todos os elementos da frente do sorteado ate o final
 * (excluindo o sorteado)
 */
long long  soma_direita(long long  sorteado, long long  JOGADORES[]) {
	long long  peso = 1;
	long long  soma = 0;
	
	for (long long  posicao = sorteado + 1; posicao < TOTAL_ATUAL; posicao++) {
		soma += JOGADORES[posicao] * peso;	
		peso ++;
	}
	return soma;
}


long long  find_posicao(long long  JOGADORES[]) {
	long long  e = 0, d = TOTAL_ATUAL - 1;
	long long  meio, soma_e, soma_d;
	
	while (e <= d) {
		meio = (e + d) / 2;
		
		soma_e = soma_esquerda(meio, JOGADORES);
		soma_d = soma_direita(meio, JOGADORES);

		if (soma_e == soma_d)
			return meio;
		
		else if (soma_e < soma_d) {
			e = meio + 1;
		}
		else {
			d = meio - 1;
		}
	}
	
	return -1;
}


int main() {
	long long  n;
	cin >> n;
	while (n != 0) {
		TOTAL_ATUAL = n;
		
		
		string NOMES[TOTAL_ATUAL];
		long long  JOGADORES[TOTAL_ATUAL];
		
		for (long long  i = 0; i < TOTAL_ATUAL; i++) {
			   cin >> NOMES[i];
			   JOGADORES[i] = soma_string(NOMES[i]);
		}
		
		long long  empate = find_posicao(JOGADORES);
		if (empate == -1)
			cout << "Impossibilidade de empate.";
		else
			cout << NOMES[empate];
		cout << "\n";
		
		cin >> n;
	}
	
	return 0;
}
