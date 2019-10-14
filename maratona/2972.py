n = int(input())

binario = str(bin(n))

print(2**binario.count('1'))