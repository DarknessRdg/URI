import math


def main():
    valor = int(input())

    raiz = int(valor ** (1/2))

    soma = 0
    fatoriais = []

    while soma <= valor:
        fatorial = math.factorial(raiz)
        if (fatorial + soma) <= valor:
            soma += math.factorial(raiz)
            fatoriais.append(raiz)
        else:
            if raiz != 0:
                raiz -= 1
            if raiz == 0:
                break

    print(len(fatoriais))


if __name__ == '__main__':
    main()
