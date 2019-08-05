def main():
    while True:
        x = int(input())

        i = 1
        for i in range(1, x + i):
            if i == x:
                print(i, end='\n')
            else:
                print(i, end=' ')

        if x == 0:
            break


if __name__ == '__main__':
    main()