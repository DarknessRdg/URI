#include <iostream>
#include "vector"
#include "set"
#include "algorithm"

#define MAX_VERTICES 50000

using namespace std;

class Aresta {

public:
    int de;
    int para;
    int peso;

    Aresta(int de, int para, int peso) {
        this->de = de;
        this->para = para;
        this->peso = peso;
    }

    static bool ordenar_por_peso(Aresta a1, Aresta a2) {
        return a1.peso < a2.peso;
    }
};




class Grafo {
    int  n;

    vector<Aresta> arestas;

    // 1 -> 2
    // 2 -> 3
    // 3 -> -1
    // 4 -> 2
    // 5 -> -1
    int conjuntos[MAX_VERTICES] {-1};

public:
    Grafo() {
        this->n = 0;
    }

    void add(int de, int para, int peso) {
        if (de > n) { n = de; }
        if (para > n) { n = para; }

        arestas.emplace_back(*new Aresta(de, para, peso));
        arestas.emplace_back(*new Aresta(para, de, peso));
    }

    void ordernar_arestas_por_peso() {
        sort(arestas.begin(), arestas.end(), Aresta::ordenar_por_peso);
    }

    void init_conjuntos() {
        for (int i = 0; i < n+1; i++) {
            conjuntos[i] = -1;
        }
    }

    int kruskal() {
        int total_pesos = 0;

        init_conjuntos();
        ordernar_arestas_por_peso();

        for (Aresta aresta: arestas) {

            auto conjunto_de = this->conjunto_de(aresta.de);
            auto conjunto_para = this->conjunto_de(aresta.para);

            if (conjunto_de != conjunto_para) {
                unir_conjuntos(conjunto_de, conjunto_para);
                total_pesos += aresta.peso;
            }
        }

        return total_pesos;
    }

    int conjunto_de(int value) {
        int conjunto_associado = conjuntos[value];

        if (conjunto_associado == -1) {
            return value;
        }
        return conjunto_de(conjunto_associado);
    }

    void unir_conjuntos(int a, int b) {
        conjuntos[a] = b;
    }
};


int main() {

    int qnt_cidades, qnt_caminhos;

    cin >> qnt_cidades;
    cin >> qnt_caminhos;

    while (true) {
        if (qnt_caminhos == qnt_cidades && qnt_caminhos == 0) {
            break;
        }

        Grafo g = *new Grafo();

        for (int i = 0; i < qnt_caminhos; i++) {
            int a, b, peso;
            cin >> a; cin >> b; cin >> peso;

            g.add(a, b, peso);
        }

        cout << g.kruskal() << endl;

        cin >> qnt_cidades;
        cin >> qnt_caminhos;
    }

    return 0;
}
