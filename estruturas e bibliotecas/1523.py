class Carro:
    def __init__(self, entrada, saida):
        self.entrada = entrada
        self.saida = saida

    def __str__(self):
        return '{} {}'.format(self.entrada, self.saida)


def main():
    q_carro, q_suportada = map(int, input().split())
    cont = 0
    while q_carro or q_suportada:
        cont += 1

        carros = []
        pilha = []

        for i in range(q_carro):
            entrada, saida = map(int, input().split())
            carros.append(Carro(entrada, saida))

        estorou = False
        for c in carros:
            if c.entrada > c.saida:
                estorou = True
                break
            elif len(pilha) == 0:
                pilha.append(c)
            else:
                while len(pilha) > 0:
                    if pilha[len(pilha) - 1].saida <= c.entrada:
                        pilha.pop()
                    else:
                        break

                if len(pilha) > 0:
                    if c.saida > pilha[len(pilha) - 1].saida:
                        estorou = True
                        break

                pilha.append(c)
            if len(pilha) > q_suportada:
                estorou = True
                break

        if estorou:
            print('Nao')
        elif len(pilha) != 0:
            error = False
            for i in range(len(pilha) - 1):
                if pilha[i].saida < pilha[i + 1].saida:
                    error = True
                    break
            if error:
                print('Nao')
            else:
                print('Sim')
        else:
            print('Sim')
        q_carro, q_suportada = map(int, input().split())


def print_(lista):
    for i in lista:
        print(i)
    print('-' * 100)


if __name__ == '__main__':
    main()
