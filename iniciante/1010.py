#produto1
digite = input()
transformar_split = digite.split()
codigo = int(transformar_split[0])
numero = int(transformar_split[1])
preço = float(transformar_split[2])
valor1 = preço * numero  
#produto2
digite2 = input()
transformar_split2 = digite2.split()
codigo2 = int(transformar_split2[0])
numero2 = int(transformar_split2[1])
preço2 = float(transformar_split2[2])
valor2 = preço2 * numero2
#Valor da compra
TOTAL = valor1 + valor2
print('VALOR A PAGAR: R$ %.2F'%TOTAL)