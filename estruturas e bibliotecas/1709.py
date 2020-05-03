def main():
    qnt = int(input())

    primeiro = 2
    cont = 1
    while primeiro != 1:
        if primeiro <= qnt/2:
            primeiro += primeiro
        else:
            primeiro -= qnt - primeiro + 1
        cont += 1
    print(cont)


if __name__ == '__main__':
    main()
