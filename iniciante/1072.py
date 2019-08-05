def main():
	#Entrada	
	N  = int(input())

	contador = 0
	dentro = 0
	fora = 0 
	
	#Processamento
	while contador < N:
		num = int(input())
		if 10 < num or num > 20:
			dentro += 1
		else:
			fora += 1
		contador +=1

	#Saida
	print(dentro, 'in')
	print(fora, 'out')
	

if __name__ == '__main__':
	main()