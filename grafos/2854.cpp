#include <iostream>
#include <map>
#include <queue>
#define null NULL
using namespace std;

class Pessoa {
public:
    string nome;
    int id;
    int vistiada;
    Pessoa(int index) { id = index; vistiada = false; nome = ""; }
};


class Conexao {
public:
    int a;
    int b;
    bool visitada;

    Conexao(int _a, int _b) {
        a = _a;
        b = _b;
        visitada = false;
    }

    bool pode_ser_usada(Pessoa* pessoa) {
        return (!visitada && (a == pessoa->id || b == pessoa->id));
    }
};


int COUNTER = 1;
int COUNTER_GROUPS = 1;
map<string, int> IDS;


int id_nome_pessoa(string __nome) {
    int id = IDS[__nome];

    if (id == 0) {
        IDS[__nome] = COUNTER;
        id = COUNTER;
        COUNTER++;
    }

    return id-1;
}

void bfs(
        Conexao* conexao[],
        int qnt_conexos,
        Pessoa* pessoas_atual,
        Pessoa* pessoas[]
) {
    pessoas_atual->vistiada = true;

    // filter
    Conexao* conexos_da_pessoa[qnt_conexos];
    int count_conexos_da_pessoa = 0;
    for (int i = 0; i < qnt_conexos; i++) {
        auto con = conexao[i];
        if (con->pode_ser_usada(pessoas_atual)) {
            conexos_da_pessoa[count_conexos_da_pessoa++] = con;
        }
    }

    for (int i = 0; i < count_conexos_da_pessoa; i++) {
        auto con = conexos_da_pessoa[i];
        con->visitada = true;

        Pessoa* outra_pessoa;
        if (pessoas_atual->id == con->a) {
             outra_pessoa = pessoas[con->b];
        } else {
            outra_pessoa = pessoas[con->a];
        }

        bfs(conexao, qnt_conexos, outra_pessoa, pessoas);
    }
}


int main() {
    int qnt_pessoas, qnt_conexoes;
    cin >> qnt_pessoas; cin >> qnt_conexoes;

    queue<int> fila;

    Conexao* conexoes[qnt_conexoes];
    Pessoa* pessoas[qnt_pessoas];

    for (int i = 0; i < qnt_pessoas; i++) {
        pessoas[i] = new Pessoa(i);
    }

    for (int i = 0; i < qnt_conexoes; i++) {
        string a, b, lixo;

        cin >> a;
        cin >> lixo;
        cin >> b;

        auto id_a = id_nome_pessoa(a);
        auto id_b = id_nome_pessoa(b);

        pessoas[id_a]->nome = a;
        pessoas[id_b]->nome = b;

        conexoes[i] = new Conexao(id_a, id_b);
    }

    for (Pessoa* p: pessoas) {
        if (!p->vistiada) {
            bfs(conexoes, qnt_conexoes, p, pessoas);
            COUNTER_GROUPS++;
        }
    }

    cout << COUNTER_GROUPS-1 << endl;



    return 0;
}
