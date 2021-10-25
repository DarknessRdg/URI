#include <iostream>
#include <map>
#define null NULL
using namespace std;

class Pessoa {
public:
    int id;
    int vistiada;
    Pessoa(int index) { id = index; vistiada = false; }
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
int COUNTER_FAMILIAS = 0;
map<string, int> IDS;


int id_nome_pessoa(string __nome) {
    int id = IDS[__nome];

    bool nao_tem_id_ainda = id == 0;
    if (nao_tem_id_ainda) {
        IDS[__nome] = COUNTER;
        id = COUNTER;
        COUNTER++;
    }

    return id-1;
}

void dfs(
        Conexao* conexao[],
        int qnt_conexos,
        Pessoa* pessoas_atual,
        Pessoa* pessoas[]
) {
    pessoas_atual->vistiada = true;

    // filter conexoes da pessoas não vistiadas ainda
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

        dfs(conexao, qnt_conexos, outra_pessoa, pessoas);
    }
}


int main() {
    int qnt_pessoas, qnt_conexoes;
    cin >> qnt_pessoas; cin >> qnt_conexoes;

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

        auto index_pessoa_a = id_nome_pessoa(a);
        auto index_pessoa_b = id_nome_pessoa(b);

        conexoes[i] = new Conexao(index_pessoa_a, index_pessoa_b);
    }

    for (Pessoa* p: pessoas) {
        if (!p->vistiada) {
            dfs(conexoes, qnt_conexoes, p, pessoas);
            COUNTER_FAMILIAS++;
        }
    }

    cout << COUNTER_FAMILIAS << endl;

    return 0;
}
