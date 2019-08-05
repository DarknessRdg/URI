def main():
    while True:
        try:
            qnt = input()
            if qnt == '':
                continue
            else:
                qnt = int(qnt)
            
            parafusos = []
            for i in range(qnt):
                x, y = map(int, input().split())
                for j in range(x, y + 1):
                    parafusos.append(j)

            parafusos.sort()

            procurar = int(input())

            inicio = len(parafusos)
            fim = 0
            cont_iguais = 0
            for i in range(len(parafusos)):
                if parafusos[i] == procurar:
                    cont_iguais += 1
                    if i < inicio:
                        inicio = i
                    if i > fim:
                        fim = i
            if cont_iguais != 0:
                print('%d found from %d to %d' %(procurar, inicio, fim))                    
            else:
                print('%d not found' %procurar)
        
        except:
            break


if __name__ == '__main__':
    main()