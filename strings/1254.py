def main():
    while True:
        try:
            old = input()
            new = input()
            entrada = input().split('<')
            for i in range(len(entrada)):
                entrada[i] = limpar(entrada[i], new, old)
            print('<'.join(entrada))
        except:
            break


def limpar(text, new, old):
    old = old.lower()
    index = text.lower().find(old)

    barra = text.find('>')
    while index != -1 and index < barra:
        text = text[:index] + new + text[index + len(old):]
        index = text.lower().find(old)
        barra = text.find('>')

    return text


if __name__ == '__main__':
    main()
