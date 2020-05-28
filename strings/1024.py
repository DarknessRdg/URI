def main():
    global frase
    n = int(input())
    for i in range(n):
        frase = list(input())
        cripto(frase)

        frase = frase[::-1]
        metade = len(frase) // 2
        for i in range(metade, len(frase)):
            frase[i] = chr(ord(frase[i]) - 1)
        print(''.join(frase))


def cripto(n):
    for i in range(len(n)):
        if 97 <= ord(n[i]) <= 122 or 65 <= ord(n[i]) <= 90:
            n[i] = chr(ord(n[i]) + 3)


if __name__ == '__main__':
    main()
