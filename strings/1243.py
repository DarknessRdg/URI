def main():
    while True:
        try:
            entrada = input().split()

            tamanho = 0
            palavra = 0
            for i in entrada:
                if eh_palavra(i):
                    tamanho += len(i) - 1 if '.' in i else len(i)
                    palavra += 1
            if palavra == 0:
                media = 0
            else:
                media = tamanho // palavra
            if media <= 3:
                print(250)
            elif media < 6:
                print(500)
            else:
                print(1000)
        except:
            break


def eh_palavra(text):
    ponto = text.find('.')

    if ponto == 0 or text.count('.') > 1:
        return False
    elif ponto != -1 and ponto < len(text) - 1:
        return False

    for i in text:
        if i == '.':
            continue
        elif not 'a' <= i.lower() <= 'z':
            return False

    return True


if __name__ == '__main__':
    main()