def main():
    while True:
        try:
            pilha = []
            ultimo = 0
            entrada = input()
            error = False
            cont_a, cont_b = 0, 0
            for i in entrada:
                if i == '(':
                    pilha.append(i)
                    ultimo += 1
                    cont_a += 1

                elif i == ')':
                    if '(' in pilha and cont_a > cont_b:
                        cont_b += 1
                        pilha.append(i)
                    else:
                        error = True
                        break

            if len(pilha) % 2  == 0 and len(pilha) != 0 and not error:
                print('correct')
            else:
                print('incorrect')



        except EOFError:
            break


if __name__ == '__main__':
    main()
