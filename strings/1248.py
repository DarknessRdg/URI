def main():
    qnt = int(input())
    for i in range(qnt):
        dieta = input()
        brekafast = input()
        almoço = input()

        comeu = brekafast + almoço

        falta_comer = ''

        if cheater(comeu, dieta):
            print('CHEATER')
        elif dieta == '':
            continue
        else:
            comeu, dieta = ordem_alfabetica(comeu, dieta)           

            for i in range(len(dieta)):
                if dieta[i] not in comeu:
                    falta_comer += dieta[i]

            print(falta_comer)



def cheater(comeu, dieta):
    if len(comeu) > len(dieta):
        return True
    else:
        for letra in comeu:
            if letra not in dieta:
                return True
    return False


def ordem_alfabetica(comeu, dieta):
    comeu_alfab = ''
    dieta_alfab = ''

    for j in range(65, 91):

        if comeu.find(chr(j)) >= 0:
            comeu_alfab += comeu[comeu.find(chr(j))]
    
    for j in range(65, 91):
        if dieta.find(chr(j)) >= 0:
            dieta_alfab += dieta[dieta.find(chr(j))]

    return comeu_alfab,  dieta_alfab

if __name__ == '__main__':
    main()
