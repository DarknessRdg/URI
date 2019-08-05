def main():
    jogadores, rodadas = map(int, input().split())
    pontos = list(map(int, input().split()))

    dic = {}
    cirar_dic(dic, jogadores)

    for i in range(0, len(pontos), jogadores):
        for item in dic:
            dic[item] += pontos[item + i - 1]

    print(vencedor(dic))



def vencedor(dic):
    maior = 0
    winner = 0
    for i in dic:
        if dic[i] >= maior:
            maior = dic[i]
            winner = i
    return winner

def cirar_dic(dic, jogadores):
    for i in range(1, jogadores + 1):
        dic[i] = 0


if __name__ == '__main__':
    main()
