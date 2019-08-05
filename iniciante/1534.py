def main():
    while True:
        try:    
            qnt = int(input())
            matriz = []
            for i in range(qnt):
                matriz += [[3] * qnt]

            diagonal_principal(matriz)
            diagonal_secundaria(matriz)
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    print(matriz[i][j], end='')
                print()
        
        except EOFError:
            break

            
def diagonal_principal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                matriz[i][j] = 1


def diagonal_secundaria(matriz):
    indice = len(matriz) - 1
    for i in range(len(matriz) - 1, -1, -1):        
        matriz[i][indice - i] = 2

if __name__ == '__main__':
    main()