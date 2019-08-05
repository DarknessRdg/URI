def main():

    lider , ultimo = map(int, input().split())

    tempo = ultimo - lider

    print(ultimo // tempo + 1 if ultimo % tempo != 0 else ultimo // tempo)


if __name__ == '__main__':
    main()
