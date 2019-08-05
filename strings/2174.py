def main():
    qnt = int(input())
    dic = []
    for i in range(qnt):
        pok = input()
        if pok not in dic:
            dic.append(pok)
    print("Falta(m) {} pomekon(s).".format(151 - len(dic)))


if __name__ == '__main__':
    main()
