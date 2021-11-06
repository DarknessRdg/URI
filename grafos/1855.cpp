#include <iostream>
#define VISITADO 'O'
#define optimize ios::sync_with_stdio(false);cin.tie(NULL)
using namespace std;


int main() {
    int j, i;
    cin >> j;
    cin >> i;

    char mapa[i][j];

    for (int a = 0; a < i; a++) {
        for (int b = 0; b < j; b++) {
            cin >> mapa[a][b];
        }
    }


    int i_atual = 0;
    int j_atual = 0;
    char direaco_atual;

    bool possivel = true;
    while (possivel) {
        if (i_atual < 0 || i_atual > i) { possivel = false; }
        if (j_atual < 0 || j_atual > j) { possivel = false; }

        if (!possivel) { break; }


        auto valor = mapa[i_atual][j_atual];

        if (valor ==VISITADO) {
            possivel = false;
            break;
        } else if (valor == '*') {
            possivel = true;
            break;
        } else if (valor == '>' || valor == '<' || valor == 'v' || valor == '^') {
            direaco_atual = valor;
            mapa[i_atual][j_atual] = VISITADO;
        }

        if (direaco_atual == '>') {
            j_atual ++;
        } else if (direaco_atual == '<') {
            j_atual --;
        } else if (direaco_atual == '^') {
            i_atual --;
        } else if (direaco_atual == 'v') {
            i_atual ++;
        }
    }

    if (possivel) {
        cout << "*";
    } else {
        cout << "!";
    }
    cout << endl;

    return 0;
}
