def main():
    num = []
    num.append(int(input()))
    num.append(int(input()))

    num.sort()

    for i in range(num[0] + 1, num[1]):
        x = i % 5
        if x == 2 or x == 3:
            print(i)

if __name__ == '__main__':
    main()
