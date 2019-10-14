n, m = map(int, input().split())

total = n * m
for i in range(1, 10):
    qnt = (total * (i / 10))
    if qnt % 1 != 0:
        qnt += 1

    qnt = int(qnt)
    if i != 9:
        print("%d" % qnt, end=' ')
    else:
        print("%d" % qnt, end='\n')
