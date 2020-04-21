n = int(input())
p1 = input()
p = [
    input()
    for i in range(n-1)
]

if n == 1:
    print(p1)
else:
    maior = ''
    for i in range(len(p1)):
        for j in range(i, len(p1)+1):
            if i == j:
                continue
            if abs(i-j) <= len(maior):
                continue
            sub = p1[i:j]

            if all([sub in palv for palv in p]):
                maior = sub

    print(maior)
