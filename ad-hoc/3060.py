a = int(input())
b = int(input())

base = a // b
resto = a % b

for i in range(b):
    if resto != 0:
        print(base + 1)
        resto -= 1
    else:
        print(base)
