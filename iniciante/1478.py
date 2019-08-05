def main():
	ordem = int(input())

	while  ordem != 0:
		
		matriz = []
		for i in range(1, ordem + 1):
			matriz += [[i] * ordem]

		for i in range(ordem):
			for j in range(ordem):
				if i == j:
					matriz[i][j] = 1
				if i < j:
					matriz[i][j] = matriz[i][j - 1] + 1
				if i > j:
					if j == 0:
						continue
					else:
						matriz[i][j] = matriz[i][j - 1] - 1

		for i in range(ordem):
			for j in range(ordem):
				matriz[i][j] = str(matriz[i][j])
				tamanho = len(matriz[i][j])
				if j == 0:
					if tamanho == 1:
						print('  ' + matriz[i][j], end='')
					elif tamanho == 2:
						print(' ' + matriz[i][j], end='')
					else:
						print(matriz[i][j], end='')
				else:
					if tamanho == 1:
						print('   ' + matriz[i][j], end='')
					elif tamanho == 2:
						print('  ' + matriz[i][j], end='')
					else:
						print(' ' + matriz[i][j], end='')
			print()
		print()

		ordem = int(input())


if __name__ == '__main__':
	main()