n = int(input())

ganhador = int(input())
ganhou = True
for i in range(n - 1):
    if int(input()) > ganhador:
        ganhou = False

if ganhou:
    print('S')
else:
    print('N')