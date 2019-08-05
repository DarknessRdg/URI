def main():
    x = int(input())

    z = int(input())
    while z <= x:
        z = int(input())

    contagem = 1
    i = x+1
    while x < z:
        x += i
        i +=1
        contagem += 1

    print(contagem)


if __name__ == '__main__':
    main()