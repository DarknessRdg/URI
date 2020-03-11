menor_preco = None
for i in range(int(input())):
    preco, grama = map(float, input().split())

    pagar = (1000 * preco) / grama
    if menor_preco is None:
        menor_preco = pagar
    elif pagar < menor_preco:
        menor_preco = pagar

print('%.2f' % menor_preco)
