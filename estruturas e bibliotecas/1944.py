def main():
    n = int(input())
    pilha = 'FACE'
    cont = 0

    for i in range(n):
        e = input().replace(' ', '')

        if pilha[len(pilha) - 4:] == e[::-1]:
            cont += 1
            pilha = pilha[:len(pilha) if len(pilha) == 4 else len(pilha) - 4]
        else:
            pilha += e

    print(cont)


if __name__ == "__main__":
    main()
