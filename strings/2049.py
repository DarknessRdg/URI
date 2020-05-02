def main():
    instancia = 1
    while True:
        try:
            assinatura = input()
            linha = input()

            if instancia > 1:
                print()

            print('Instancia', instancia)
            if assinatura in linha:
                print('verdadeira')
            else:
                print('falsa')
            instancia += 1

        except:
            break


if __name__ == '__main__':
    main()
