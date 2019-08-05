def main():
    cont = 0;
    while True:
        n = int(input())
        if n == 0:
            break;
        elif cont != 0:
            print()
        entrada = []
        maior = 0
        for i in range(n):
            entrada1 = input()
            entrada.append(entrada1)

        maior = max([len(i) for i in entrada])

        for i in entrada:
            print('{}{}'.format(' ' * (maior - len(i)), i))
        cont += 1

if __name__ == '__main__':
    main()