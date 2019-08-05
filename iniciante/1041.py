def main():
	#Entrada
	x, y = input().split()
	x1 = float(x)
	y1 = float(y)
	#Processamento
	#Saída
	if x1 == 0 and y1 == 0:
		print('Origem')
	elif x1 ==0:
		print('Eixo Y')
	elif y1 == 0:
		print('Eixo X')
	else:
		if x1 > 0 and y1 >0:
			print('Q1')
		elif x1 < 0 and y1 >0:
			print('Q2')
		elif x1 <0 and y1<0:
			print('Q3')
		else:
			print('Q4') 	
if __name__ == '__main__':
	main()