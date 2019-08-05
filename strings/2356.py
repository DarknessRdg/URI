def main():
    while True:
        try:
            bac = input()
            res = input()

            if res in bac:
                print('Resistente')
            else:
                print('Nao resistente')
        except:
            break


if __name__ == '__main__':
    main()
