def main():
	#Entrada	
	N  = int(input())

	contador = 1
	
	#Processamento
	while contador <= N:
		if (contador % 2) == 0 :
			print('%d^2 ='%contador , (contador**2))
		contador += 1		

	#Saida
	

if __name__ == '__main__':
	main()