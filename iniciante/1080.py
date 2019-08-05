def main():
	contador = 0	
	posição = 0
	maior = 0

	while  contador < 100:
		num_entrada = int(input())
		contador += 1		
		if contador == 1:
			maior = num_entrada
			posição = 1
		elif num_entrada > maior:
			maior = num_entrada
			posição = contador 

		else:
			maior = maior

	print(maior)
	print(posição)



if __name__ == '__main__':
	main()