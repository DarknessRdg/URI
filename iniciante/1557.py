def main():
	ordem = int(input())
	
	while ordem != 0:	

		matriz = []
		num =1
		for i in range(ordem):
			matriz += [[num] * ordem]
			num *= 2

		for i in range(ordem):
			for j in range(1, ordem):
				matriz[i][j] = matriz[i][j - 1] * 2

		maior = len(str(matriz[ordem - 1][ordem - 1]))
		
		for i in range(ordem):
			for j in range(ordem):
				tamanho_num = len(str(matriz[i][j]))
				if j == ordem - 1:
					print(' ' * (maior - tamanho_num) + str(matriz[i][j]), end='')
				else:
					print(' ' * (maior - tamanho_num) + str(matriz[i][j]), end=' ')
			print()

		print()
		ordem = int(input())

if __name__ == '__main__':
	main()
