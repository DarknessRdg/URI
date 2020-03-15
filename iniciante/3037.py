def sum_entrada():
    sum = 0
    for i in range(3):
        d, x = map(int, input().split())
        sum += d * x
    return sum


for i in range(int(input())):
    joao = sum_entrada()
    maria = sum_entrada()

    if joao > maria:
        print('JOAO')
    else:
        print('MARIA')
