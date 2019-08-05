def main():
    while True:
        try:
            rastro = list(input())
            qnt = int(input())

            cont_w = 0
            cont_r = 0
            for letra in rastro:

                if letra == 'W':
                    cont_w += 1
                    if 0 < cont_r <= qnt:
                        cont_w += 1
                    cont_r = 0
                elif letra == 'R':
                    if cont_r == qnt:
                        cont_w += 1
                        cont_r = 1
                    else:
                        cont_r += 1

            if cont_r != 0:
                cont_w += 1
            print(cont_w)
        except:
            break

if __name__ == '__main__':
    main()
