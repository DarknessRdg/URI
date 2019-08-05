def main():
    # Entrada
    linhas = int(input())
    contador = 1
    #Processamento
    for i in range(linhas):
        print(contador, contador**2, contador**3)
        contador+=1

if __name__ == '__main__':
    main()