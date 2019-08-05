def main():
    while True:
        try:
            x = int(input())
            for j in range(x):
                entrada = input()
                metade = len(entrada) // 2
                
                x = entrada[:metade]
                print(x[::-1], end='')

                x = entrada[metade:]
                print(x[::-1])

        except EOFError:
            break


if __name__ == '__main__':
    main()
