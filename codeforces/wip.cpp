#include "iostream"
#include "vector"

#define MAX_INT 112245
using namespace std;

int SOMA_ACUMULADA[MAX_INT];


/**
 * Implementação usando uma lógica heap
 */
int query(int id_do_no, int left, int right, int query_left, int query_right) {
    bool eh_folha = left == right;
    if (eh_folha) return SOMA_ACUMULADA[id_do_no];

    bool esta_contido_na_query = query_left <= left
                                 && right <= query_right;

    if (esta_contido_na_query) return SOMA_ACUMULADA[id_do_no];

    bool esta_fora_da_query = query_right < left
                              || right < query_left;
    if (esta_fora_da_query) return 0;

    // Nesse ponto, isso signfica que a query está entre nós de duas subarvores
    // diferentes
    //           a
    //     b          c
    //   d   e      f   g
    //
    // por ex: do "e" ao "g"

    int meio = (left + right) / 2;

    int filho_da_esquerda = 2 * id_do_no;
    int filho_da_direita = (2 * id_do_no) + 1;
    return query(filho_da_esquerda, left, meio, query_left, query_right)
           + query(filho_da_direita, meio + 1, right, query_left, query_right);
}


void update(
        int id_do_no,
        int left,
        int right,
        int posicao_para_atualizar,
        int novo_valor
) {
    bool eh_a_folha_para_atualizar = left == right;

    if (eh_a_folha_para_atualizar) {
        SOMA_ACUMULADA[id_do_no] = novo_valor;
        return;
    }

    // precisa ir para a arvore da esquerda ou da direita até chegar no filho
    int meio = (left + right) / 2;

    bool eh_filho_da_esquerda = posicao_para_atualizar <= meio;

    int filho_esquerd = 2 * id_do_no;
    int filho_da_direita = (2 * id_do_no) + 1;

    if (eh_filho_da_esquerda) {
        update(filho_esquerd, left, meio, posicao_para_atualizar, novo_valor);
    } else {
        update(filho_da_direita, meio+1, right, posicao_para_atualizar, novo_valor);
    }

    // autliza o valor da soma acumulada do nó
    // que é a soma da esquerda + direita
    SOMA_ACUMULADA[id_do_no] = SOMA_ACUMULADA[filho_esquerd] + SOMA_ACUMULADA[filho_da_direita];
}


int main() {
    int qnt_prato, qnt_operacoes;
    cin >> qnt_prato;
    cin >> qnt_operacoes;

    vector<int> pratos(qnt_prato, 0);

    for (int i = 0; i < qnt_operacoes; i++) {
        int t;
        cin >> t;
        if (t == 1) {
            int p;
            cin >> p;

            // insert p

        } else {
            int l, r;
            cin >> l,
                    cin >> r;

            // mostra cont da query
        }
    }
    return 0;
}
