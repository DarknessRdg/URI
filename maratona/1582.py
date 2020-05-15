def mdc(num1, num2):
    resto = None
    while resto is not 0:
        resto = num1 % num2
        num1 = num2
        num2 = resto

    return num1


def eh_triangulo(a, b, c):
    return abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b


def eh_reto(a, b, c):
    lados = [a, b, c]
    hipo = max(lados)
    
    lados.remove(hipo)
    
    return hipo**2 == lados[0]**2 + lados[1]**2
    

def main():
    a, b, c = map(int, input().split())
    
    m1 = mdc(a, c)
    m2 = mdc(a, b)
    m3 = mdc(b, c)
    
    if m1 == 1 and m2 == 1 and m3 == 1 and eh_triangulo(a, b, c) and eh_reto(a, b, c):
        print('tripla pitagorica primitiva')
    elif m1 == m2 and m1 == m3 and m2 == m3 and eh_triangulo(a, b, c) and eh_reto(a, b, c):
        print('tripla pitagorica')
    else:
        print('tripla')


if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            break
