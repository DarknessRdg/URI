def main():
    qnt = int(input())
    montanhas = list(map(int, input().split()))

    print(test(montanhas))


def test(montanhas):
    tam = len(montanhas)
    if tam == 1:
        return 1
    elif tam == 2:
        return 1 if montanhas[0] != montanhas[1] else 0
    
    maior = montanhas[0] > montanhas[1]
    for i in range(1, tam - 1):
        if maior and montanhas[i] >= montanhas[i + 1]:
            return 0
        if not maior and montanhas[i] <= montanhas[i + 1]:
            return 0
        maior = not maior

    return 1


if __name__ == "__main__":
    main()