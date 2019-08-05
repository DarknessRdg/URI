def main():
    risada = list(input())
    risada_limpa = []
    for letra in risada:
        if letra in ['a', 'e', 'i', 'o', 'u']:
            risada_limpa.append(letra)

    if risada_limpa == risada_limpa[::-1]:
        print('S')
    else:
        print('N')


if __name__ == '__main__':
    main()
