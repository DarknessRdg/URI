def main():
	coluna = int(input())
	operaçao = input()

	if operaçao == 'S':
			
		matriz = []
		for i in range(12):
			matriz += [[0] * 12]
		for i in range(12):
			for j in range(12):
				matriz[i][j] = float(input())

		soma = 0
		for i in range(12):
			for j in range(12):
				if j == coluna:
					soma += matriz[i][j]
		print('%.1f' %soma)

	else:
		matriz = []
		for i in range(12):
			matriz += [[0] * 12]
		for i in range(12):
			for j in range(12):
				matriz[i][j] = float(input())

		media = 0
		for i in range(12):
			for j in range(12):
				if j == coluna:
					media += matriz[i][j]
		media /= 12

		print('%.1f' %media)


if __name__ == '__main__':
	main()