#include <iostream>
#include <vector>
#include <algorithm>
#define optimize ios::sync_with_stdio(false);cin.tie(NULL)
#define NAO_USADO -1
using namespace std;

class Tarefa {
public:
    int valor, tempo, index;
    bool usada;

    Tarefa(int valor, int tempo, int index) {
        this->valor = valor; this->tempo = tempo; this->index = index;
        usada = false;
    }

    void usar() { usada = true; }
};

bool ordenar_por_valor(Tarefa* a1, Tarefa* a2) {
    return a1->valor > a2->valor;
}

int posicao_disponivel_para_usar(vector<int> tarefas_usadas, Tarefa* tarefa) {
    int index = tarefa->tempo - 1;

    while (index >= 0 && tarefas_usadas[index] != NAO_USADO) {
        index--;
    }
    return index;
}

void escolher_tarefas(vector<int> tarefas_usadas, const vector<Tarefa*>& tarefas) {
    for (auto tarefa: tarefas) {
        if (!tarefa->usada) {

            auto posicao = posicao_disponivel_para_usar(tarefas_usadas, tarefa);

            if (posicao >= 0) {
                tarefas_usadas[posicao] = 1;
                tarefa->usar();
            }
        }
    }
}

bool test_case() {
    int n_tarefas, n_horas;

    if (!(cin >> n_tarefas) || !(cin >> n_horas)) {
        return false;
    }

    vector<int> tarefas_pegas(n_horas, NAO_USADO);

    vector<Tarefa*> tarefas;

    int v, t;
    for (int i = 0; i < n_tarefas; i++) {
        cin >> v;
        cin >> t;

        tarefas.emplace_back(new Tarefa(v, t, i));
    }

    sort(tarefas.begin(), tarefas.end(), ordenar_por_valor);

    escolher_tarefas(tarefas_pegas, tarefas);

    int ans = 0;
    for (auto tarefa: tarefas) {
        if (!tarefa->usada) {
            ans += tarefa->valor;
        }
    }
    cout << ans << endl;

    return true;
}

int main() {
    while (test_case()) {}

    return 0;
}
