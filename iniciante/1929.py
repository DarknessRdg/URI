from itertools import permutations


def main():

    tam = list(map(int, input().split()))
    bool = False
    for subset in permutations(tam, 3):
        if verificar(subset):
            bool = True
            break
    print('S' if bool else 'N')


def verificar(array):
    a = array[0]
    b = array[1]
    c = array[2]
    return (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b


if __name__ == '__main__':
    main()