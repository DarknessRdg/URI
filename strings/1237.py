def main():
    while True:
        try:

            entrada1 = input()
            entrada2 = input()

            x = comparacao(entrada1, entrada2)
            print(x)


        except:
            break

def comparacao(p1, p2):
    tam = 0
    maior = []
    while tam <= max(len(p1), len(p2)):

        for i in range(len(p2)):
            x = p2[i:tam]

            if x == '':
                break
            elif x in p1:

                maior.append(len(x))
                continue


        tam += 1

    if len(maior) == 0:
        return 0
    else:
        return max(maior)


if __name__ == '__main__':
    main()