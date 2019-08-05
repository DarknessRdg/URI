def main():
    interruptores, lampadas = map(int, input().split())
    acesas = [False for i in range(lampadas)]

    entrada = list(map(int, input().split()))
    for i in range(1, len(entrada)):
        acesas[entrada[i] - 1] = True

    qnt = 0
    inicio = list(acesas)
    acoes = []
    for i in range(interruptores):
        acoes.append(list(map(int, input().split()))[1:])

    terminou = True

    while terminou:
        for inter in acoes:

            for i in inter:
                acesas[i - 1] = trocra(acesas[i - 1])
            qnt += 1

            if True not in acesas:
                terminou = False
                break

        if acesas == inicio:
            terminou = False
            qnt = -1
            break

    print(qnt)


def trocra(a):
    return not a


if __name__ == '__main__':
    main()
