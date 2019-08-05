def main():
    # contadores
    contador = 1
    vit_inter = 0
    vit_gremio = 0
    empate = 0

    campeao = None
    while True:
        # Entrada
        inter, gremio = map(int, input().split())

        # Processamento
        if inter > gremio:
            vit_inter += 1
        elif inter < gremio:
            vit_gremio += 1
        else:
            empate += 1
        continua = input('Novo grenal (1-sim 2-nao)\n')

        if vit_inter > vit_gremio:
            campeao = 'Inter venceu mais'
        elif vit_inter < vit_gremio:
            campeao = 'Gremio venceu mais'
        else:
            campeao = 'Nao houve vencedor'

        if continua == '1':
            contador += 1
            continue

        elif continua == '2':
            print(contador, 'grenais')
            print('Inter:%d' % vit_inter)
            print('Gremio:%d' % vit_gremio)
            print('Empates:%d' % empate)
            print(campeao)
            break


if __name__ == '__main__':
    main()