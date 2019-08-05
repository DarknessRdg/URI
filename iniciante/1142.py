def main():
    # Entrada
    linhas = int(input())
    contador = 0
    #Processamento
    for i in range(linhas):
        print(contador + 1, contador + 2, contador + 3, end=' PUM\n')
        contador += 4

if __name__ == '__main__':
    main()