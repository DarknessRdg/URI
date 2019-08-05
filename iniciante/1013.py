valores = input()
splitados = valores.split()
a = int(splitados[0])
b = int(splitados[1])
c = int(splitados[2])

MaiorAB = (a+b+(abs(a-b)))/2
MaiorAC = (a+c+(abs(a-c)))/2
Maior = (MaiorAB + MaiorAC + (abs(MaiorAB-MaiorAC)))/2

print('%.0f'%Maior, 'eh o maior')