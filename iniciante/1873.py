PEDRA, PAPEL, TESOURA, LAGARTO, SPOCK, EMPATE = 'pedra', 'papel', 'tesoura', 'lagarto', 'spock', 'empate'


def pedra_ganha_de(x):
    return x == TESOURA or x == LAGARTO 


def tesoura_ganha_de(x):
    return x == PAPEL or x == LAGARTO


def papel_ganha_de(x):
    return x == PEDRA or x == SPOCK


def spock_ganha_de(x):
    return x == TESOURA or x == PEDRA


def lagarto_ganha_de(x):
    return x == SPOCK or x == PAPEL


def regra(x, y):
    if x == y:
        return EMPATE

    if x == PEDRA:
        if pedra_ganha_de(y):
            return x
        else:
            return y


    elif x == TESOURA:
        if tesoura_ganha_de(y):
            return x
        else:
            return y

    elif x == PAPEL:
        if papel_ganha_de(y):
            return x
        else:
            return y
    

    elif x == LAGARTO:
        if lagarto_ganha_de(y):
            return x
        else:
            return y

    elif x == SPOCK:
        if spock_ganha_de(y):
            return x
        else:
            return y

def main():
    c = int(input())
    for i in range(c):
        raj, sheldon = input().split()
    
        ganhador = regra(raj, sheldon)

        if ganhador == raj:
            print('rajesh')
        elif ganhador == sheldon:
            print('sheldon')
        else:
            print('empate')


if __name__ == "__main__":
    main()