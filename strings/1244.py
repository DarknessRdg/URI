def main():
    n = int(input())
    for i in range(n):
        entrada = sorted(input().split(), key=lambda palavra: len(palavra), reverse=True)

        print(' '.join(entrada))


if __name__ == '__main__':
    main()
