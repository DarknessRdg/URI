def main():
    caso = 0
    while True:
        caso += 1
        try:
            
            entrada = input()
            procurar = input()
            tam = len(entrada)
            
            cont = 0
            index = 0
            for i in range(len(procurar)):
                if procurar[i:tam + i] == entrada:
                    cont += 1
                    index = i

            print('Caso #{}:'.format(caso))
            if cont == 0:
                print('Nao existe subsequencia')
            else:
                print('Qtd.Subsequencias:', cont)
                print('Pos:', index + 1)
            print()
        except:
            break

if __name__ == "__main__":
    main()