def main():
    qnt = 0
    vezes = input()
    while True:
        try:
            entrada = int(input())
            if entrada != 1:
                qnt += 1
        except:
            break
    print(qnt)


if __name__ == '__main__':
    main()