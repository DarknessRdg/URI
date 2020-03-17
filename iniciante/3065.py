def main():
    teste = 1
    n = int(input())
    while n != 0:
        pilha = []
        entrada = input()

        numeros = list(map(int, entrada.replace('+', ' ').replace('-', ' ').split()))
        operadores = [i for i in entrada if i == '+' or i == '-']

        pilha.append(numeros.pop(0))
        n -= 1
        while n != 0:
            op = operadores.pop(0)
            pilha.append(numeros.pop(0))

            n1 = pilha.pop(0)
            n2 = pilha.pop(0)

            if op == '+':
                pilha.append(n1 + n2)
            else:
                pilha.append(n1 - n2)
            n -= 1

        print('Teste', teste)
        print(pilha.pop(0))
        print()
        n = int(input())
        teste += 1


if __name__ == '__main__':
    main()
