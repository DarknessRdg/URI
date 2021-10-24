a, b, c, d = sorted(map(int, input().split()))

if a / c == b / d:
    print('S')
elif a / b == c / d:
    print('S')
else:
    print('N')
