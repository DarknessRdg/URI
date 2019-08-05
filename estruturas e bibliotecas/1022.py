from fractions import Fraction


def main():
    n = int(input())
    for i in range(n):
        questao()


def questao():
    def convert(x):
        try:
            return int(x)
        except:
            return x

    n1, lixo1, d1, op, n2,  lixo2, d2 = map(convert, input().split())

    if op == '+':
        total = str(n1 * d2 + n2 * d1) + '/' + str(d1 * d2)
        fracao = Fraction(n1, d1) + Fraction(n2, d2)

    elif op == '-':
        total = str(n1 * d2 - n2 * d1) + '/' + str(d1 * d2)
        fracao = Fraction(n1, d1) - Fraction(n2, d2)

    elif op == '*':
        total = str(n1 * n2) + '/' + str(d1 * d2)
        fracao = Fraction(n1, d1) * Fraction(n2, d2)

    else:
        total = str(n1 * d2) + '/' + str(n2 * d1)
        fracao = Fraction(n1, d1) / Fraction(n2, d2)

    string = fracao.__str__()
    if string == '0' or not '/' in string:
        if string == 0:
            fracao = total
        else:
            fracao = string + '/1'

    print(total, '=', fracao)


if __name__ == '__main__':
    main()