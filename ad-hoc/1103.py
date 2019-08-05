def main():
    h1, m1, h2, m2 = map(int, input().split())
    while h1 != 0 or m1 != 0  or h2 != 0 or  m2 != 0:
        minuto1 = h1 * 60 + m1
        minuto2 = h2 * 60 + m2

        if minuto1 > minuto2:
            minuto2 += 24 * 60
        print(abs(minuto1 - minuto2))

        h1, m1, h2, m2 = map(int, input().split())

if __name__ == "__main__":
    main()