import sys
sys.setrecursionlimit(5000)


class Pessoa:
    def __init__(self, valor):
        self.valor = valor
        self.amigs = []
        self.contado = False


def main():
    amgs, amz = map(int, input().split())

    pessoas = [
        Pessoa(int(input()))
        for _ in range(amgs)
    ]

    for _ in range(amz):
        a, b = map(int, input().split())

        pessoas[a].amigs.append(pessoas[b])
        pessoas[b].amigs.append(pessoas[a])

    for pessoa in pessoas:
        if not pessoa.contado:
            total = soma_amizades(pessoa)
            if total != 0:
                return False
    return True


def soma_amizades(pessoa):
    total = pessoa.valor
    pessoa.contado = True

    for amz in pessoa.amigs:
        if not amz.contado:
            total += soma_amizades(amz)
    return total


if __name__ == '__main__':
    rs = main()
    if rs:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
