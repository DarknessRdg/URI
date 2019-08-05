def main():
    i = 0

    while i <= 2:
        print('I={} J={}'.format(i, 1 + i))
        print('I={} J={}'.format(i, 2 + i))
        print('I={} J={}'.format(i, 3 + i))

        i = round(i + 0.2, 2)
        if i % 1 == 0:
            i = int(i)


if __name__ == '__main__':
    main()
