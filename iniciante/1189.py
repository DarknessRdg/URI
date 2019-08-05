def main():
    operação = input().upper()
    
    matriz = []
    for i in range(12):
        matriz += [[0] * 12]

    for i in range(12):
        for j in range(12):
            matriz[i][j] = float(input())

    if operação == 'S':
        soma = 0
        for i in range(12):
            indice_secundaria = 12
            indice_secundaria -= 1
            for j in range(12):
                if i < indice_secundaria and i > j:
                    soma += matriz[i][j]
                indice_secundaria -= 1
        print('%.1f' %soma)
    else:
        media = 0
        divisao = 0
        for i in range(12):
            indice_secundaria = 12
            indice_secundaria -= 1
            for j in range(12):
                if i < indice_secundaria and i > j:
                    media += matriz[i][j]
                    divisao += 1
                indice_secundaria -= 1
        media = media/divisao

        print('%.1f' %media)


if __name__ == '__main__':
    main()