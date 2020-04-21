q = {}
matriz = [[0 for j in range(550)] for i in range(550)]

caiu = 0
for i in range(int(input())):
    x, y = map(int, input().split())

    matriz[x][y] += 1

    n = matriz[x][y]
    if n == 2:
        caiu = 1

print(caiu)
