def main():
    n = int(input())
    soma = 0
    qnt = 0
    while n >= 0:
        soma += n
        qnt += 1
        n = int(input())
    if qnt == 0 :
        print('0.00')
    else:
        print('{:.2f}'.format(soma / qnt))


if __name__ == "__main__":
    main()