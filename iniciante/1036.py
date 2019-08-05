def main():
	#Entrada
	a1, b1, c1  = input().split()
	a = float(a1)
	b = float(b1)
	c = float(c1)
	#Processamento
	if a != 0:
		delta = b**2 -4*a*c
		if delta > 0:
			import math
			R1 = (-b + math.sqrt(delta) )/(2*a)
			R2 = (-b - math.sqrt(delta) )/(2*a)
			print('R1 = %.5f' %R1)
			print('R2 = %.5f' %R2)
		else:
			print('Impossivel calcular')
	else:
		print('Impossivel calcular')		
	#Saída

if __name__ == '__main__':
	main()