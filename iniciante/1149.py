def main():
    entrada = input().split()
    qtd = len(entrada)

    a = int(entrada[0])
    n = int(entrada[1])

    indice = 2
    while n <= 0:
        n = int(entrada[indice])
        indice += 1

    somador = 0

    for i in range(n):
        somador += (i + a)

    print(somador)


if __name__ == '__main__':
    main()