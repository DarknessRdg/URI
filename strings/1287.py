def overflow(numero):
    max = 2147483647
    return int(numero) > max


def main():
    while True:
        try:
            entrada = input()

            saida = ''
            invalido = False
            for i in entrada:
                if i.lower() == 'o':
                    saida += '0'
                elif i == 'l':
                    saida += '1'
                elif '0' <= i <= '9':
                    saida += i
                elif i in (',', ' '):
                    continue
                else:
                    invalido = True
                    break

            if saida == '' or invalido:
                print('error')
            elif overflow(saida):
                print('error')
            else:
                print(str(int(saida)))
        except:
            break


if __name__ == '__main__':
    main()
