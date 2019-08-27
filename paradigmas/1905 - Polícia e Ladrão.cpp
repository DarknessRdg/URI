#include <iostream>
using namespace std;

bool winner;

int LIMITE_SUP = 5; 
int LIMITE_INF = 0;

int ESCONDERIJO = 4;

bool dentro_da_matriz(int i) {
	  return i >= LIMITE_INF && i < LIMITE_SUP;	
}

bool achou_os_ladroes(int i, int j) {
	return i == ESCONDERIJO && j == ESCONDERIJO;
}

bool caminho_livre(int x) {
	return x == 0;
}

void busca(int matriz[5][5], bool visitidados[5][5], int i, int j) {
	if (!visitidados[i][j] && dentro_da_matriz(i) && dentro_da_matriz(j)) {
		
		visitidados[i][j] = true;
		if (achou_os_ladroes(i, j)) {
			winner = true;
			return;
		}
		
		int vertical = i + 1; // cima / baixo
		if (dentro_da_matriz(matriz[vertical][j]) && caminho_livre(matriz[vertical][j]))
			busca(matriz, visitidados, vertical, j);
		
		vertical = i - 1;
		if (dentro_da_matriz(matriz[vertical][j]) && caminho_livre(matriz[vertical][j]))
			busca(matriz, visitidados, vertical, j);
		
		int horizontal = j + 1; // direita / esquerda
		if  (dentro_da_matriz(matriz[i][horizontal]) && caminho_livre(matriz[i][horizontal]))
			busca(matriz, visitidados, i, horizontal); 
		
		horizontal = j - 1;
		if  (dentro_da_matriz(matriz[i][horizontal]) && caminho_livre(matriz[i][horizontal]))
			busca(matriz, visitidados, i, horizontal); 
	}
}

int main() {
	int loops;
	cin >> loops;
	for (int q = 0; q < loops; q++) {
		
		winner = false;		
		int matriz[5][5];
		bool vistidados[5][5];
		
		for (int i = 0; i < LIMITE_SUP; i++) {
			for (int j = 0; j < LIMITE_SUP; j++) {
				cin >> matriz[i][j];
				vistidados[i][j] = false;
			}
		}
		
		busca(matriz, vistidados, 0, 0);
		
		if (winner) cout << "COPS" << endl;
		else cout << "ROBBERS" << endl;
	}
	
	return 0;
}