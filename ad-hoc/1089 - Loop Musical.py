def subindo(anterior, atual):
    return anterior < atual


def descendo(anterior, atual):
    return anterior > atual


def main():
    n = int(input())
    while n:
        coodenadas = list(map(int, input().split()))
        coodenadas.append(coodenadas[0])

        cont = 0
        i = 1
        while i < len(coodenadas):
            subiu = False
            desceu = False
            while i < len(coodenadas) and subindo(coodenadas[i - 1], coodenadas[i]):  # while subindo
                i += 1
                subiu = True

            while i < len(coodenadas) and descendo(coodenadas[i - 1], coodenadas[i]):  # while descendo
                i += 1
                desceu = True

            if not (subiu and desceu):
                # tenta subir dnv
                while i < len(coodenadas) and subindo(coodenadas[i - 1], coodenadas[i]):  # while subindo
                    i += 1
                    subiu = True
            if subiu and desceu:
                cont += 1
            if desceu and subiu:
                cont += 1
        print(cont)
        n = int(input())


if __name__ == '__main__':
    main()
