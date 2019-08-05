def main():
    creditos = list(map(int, input().split()))
    creditos.sort()

    if dois_iguais(creditos) or soma(creditos):
        print('S')
    else:
        print('N')


def soma(creditos):
    maior = max(creditos)
    soma = 0
    for i in creditos:
        if i != maior:
            soma += i
    if soma == maior:
        return True
    else:
        return False


def dois_iguais(creditos):
    for i in range(len(creditos) - 1):
        if creditos[i] == creditos[i + 1]:
            return True

    return False


if __name__ == '__main__':
    main()
