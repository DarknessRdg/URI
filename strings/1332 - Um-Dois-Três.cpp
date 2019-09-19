#include <iostream>
using namespace std;


bool igual(string e, string correto) {
	if (e.length() != correto.length())
		return false;
	
	int cont = 0;
	for(int i = 0; correto[i] != '\0'; i++) {
		if (correto[i] == e[i])
			cont += 1;
	}
	
	return cont == correto.length() || cont == correto.length() - 1;
}


int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string entrada;
		cin >> entrada;
		
		if (igual(entrada, "one"))
			cout << "1";
		else if (igual(entrada, "two"))
			cout << "2";
		else 
			cout << "3";
		cout << endl;
				
		
	}
	
	
	return 0;
}