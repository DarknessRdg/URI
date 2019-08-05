def main():
    j = int(input())

    while j != 0:
        x = []
        maior = 0
        for i in range(j):
            entrada = ' '.join(input().split())
            if len(entrada) > maior:
                maior = len(entrada)
            x.append(entrada)

        if len(x) == 0:
            print(' ')
        else:
            for i in x:
                print(i.rjust(maior))

        j = int(input())
        if j != 0:
            print()

if __name__ == '__main__':
    main()
