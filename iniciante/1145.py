def main():
    x, y = input().split()
    x = int(x)
    y = int(y)

    contador = x

    for i in range(1,y + 1):
        if contador == 1:
            print(i)
            contador = x
        else:
            print(i, end=' ')
            contador -= 1


if __name__ == '__main__':
    main()