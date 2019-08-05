def main():
    qnt = int(input())
    for i in range(qnt):
        x = int(input())
        idiomas = []
        for j in range(x):
            y = input()
            if y not in idiomas:
                idiomas.append(y)
        print(verificar(idiomas))


def verificar(a):
    for i in range(len(a) - 1):
        if a[i] != a[i + 1]:
            return 'ingles'
    return a[0]

if __name__ == '__main__':
    main()
