#include<bits/stdc++.h>
using namespace std;

int abs(int n) {
    if (n < 0) return -n;
    else return n;
}

bool eh_triangul(int a, int b, int c) {
    if (abs(b - c) < a && a < b  + c)
        return true;
    else if (abs(a - c) < b && b < a + c)
        return true;
    else if (abs(a - b) < c && c < a + b)
        return true;
    else 
        return false;
}

int qnt_iguais(int vetor[]) {
    int cont = 0;
    for(int i = 0; i < 3; i ++) {
        bool tem_igual = false;
        
        for (int j = 0; j < 3; j++) {
            if (vetor[i] == vetor[j] && j != i) {
                tem_igual = true;
                break;
            }
        }

        if (tem_igual)
            cont ++;
    }

    return cont;
}

bool eh_retangulo(int a, int b, int c) {
    return a*a == b*b + c*c || b*b == a*a + c*c || c*c == a*a + b*b;
}

int main() {
    int x, y, z;
    cin >> x >> y >> z;
    
    if (eh_triangul(x, y, z)) {
        int vetor[] = {x, y, z};
        int iguais = qnt_iguais(vetor);
        
        if (iguais == 0)
            cout << "Valido-Escaleno" << endl;
        else if (iguais == 2)
            cout << "Valido-Isoceles" << endl;
        else
            cout << "Valido-Equilatero" << endl;

        cout << "Retangulo: ";
        if (eh_retangulo(x,y,z)) cout << "S";
        else cout << "N";
        cout << endl;
    }
    
    else
        cout << "Invalido" << endl;

    return 0;
}