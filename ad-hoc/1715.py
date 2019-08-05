def main():
    jogadores, partidas = map(int, input().split())

    dic = {}
    for i in range(jogadores):
        dic[i] = list(map(int, input().split()))

    qnt = 0
    for jogador in dic:
        if 0 not in dic[jogador]:
            qnt += 1

    print(qnt)


if __name__ == '__main__':
    main()
