def main():
	#Entrada
	num1 , num2, num3 = input().split()

	a = float(num1)
	b = float(num2)
	c = float(num3)
	#Processamento:
		#A é o maior
	if a >= b and a >= c:
		maior = a
		meio = b
		menor = c
	elif b >=a and b>=c:
		maior = b
		meio = a
		menor = c
	else:
		maior = c
		meio = a 
		menor = b
	#Saida
		#CONDIÇOES URI
	if maior >= meio+menor:
		print('NAO FORMA TRIANGULO')
	else:
		if maior**2 == (meio**2 + menor**2):
			print('TRIANGULO RETANGULO')
		
		if maior**2 > (meio**2 + menor**2):
			print('TRIANGULO OBTUSANGULO')
		
		if maior**2 < (meio**2 + menor**2):
			print('TRIANGULO ACUTANGULO')
		
		if a == b == c:
			print('TRIANGULO EQUILATERO')
		elif a ==b or a == c or b ==c :
			print('TRIANGULO ISOSCELES')

		
if __name__ == '__main__':
	main()