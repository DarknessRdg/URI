x = int(input())
while x != 0:
    start = x if x % 2 == 0 else x + 1
    print(5 * start + 20)

    x = int(input())
