def main():
    while True:
        try:
            dodo, leo, peper = map(primeiras, input().split())
            if wins(dodo, leo, peper):
                print('Os atributos dos monstros vao ser inteligencia, sabedoria...')   
            elif wins(leo, dodo, peper):
                print("Iron Maiden's gonna get you, no matter how far!")
            elif wins(peper, leo, dodo):
                print('Urano perdeu algo muito precioso...')
            else:
                print('Putz vei, o Leo ta demorando muito pra jogar...')
        except:
            break


def wins(firts, other_1, other_2):
    if firts == 'pe':
        return other_1 == 'te' and other_2 == 'te'
    elif firts == 'pa':
        return other_1 == 'pe' and other_2 == 'pe'
    elif firts == 'te':
        return other_1 == 'pa' and other_2 == 'pa'

def primeiras(x):
    return x[0] + x[1]


if __name__ == "__main__":
    main()