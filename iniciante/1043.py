def main():
	#Entrada
	num1, num2, num3 = input().split()
	a = float(num1)
	b = float(num2)
	c = float(num3)
	#Processamento:
	#Trigangulo?
	soma1 = a + b
	soma2 = b + c
	soma3 = a + c
	#Saida
	if (abs(a-b)<c and c< soma1) or (abs(b-c)<c  and a<soma2) or (abs(a-c)<b and b<soma3):
		perimetro = a + b + c
		print('Perimetro =', perimetro)
	else:
		area = (a+b)*c /2 
		print('Area = %.1f' %area) 


if __name__ == '__main__':
	main()