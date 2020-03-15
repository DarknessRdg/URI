def main():
    n, a = map(int, input().split())
    while n != 0 and a != 0:
        maria = set(map(int, input().split()))
        alice = set(map(int, input().split()))

        intersection = maria.intersection(alice)
        maria = len(maria.difference(intersection))
        alice = len(alice.difference(intersection))

        if maria > n or maria > a:
            print(alice)
        elif alice > n or alice > a:
            print(maria)
        else:
            print(min([maria, alice]))

        n, a = map(int, input().split())


if __name__ == '__main__':
    main()
