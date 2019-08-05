def main():
	operação = input()
	if operação == 'S':
		matriz = []
		for i in range(12):
			matriz += [[0] * 12]
		for i in range(12):
			for j in range(12):
				matriz[i][j] = float(input())

		soma = 0
		fim = 11
		for i in range(12):
			for j in range(12):
				if j > fim:
					soma += matriz[i][j]
			fim -= 1

		print('%.1f' %soma)		

	else:
		matriz = []
		for i in range(12):
			matriz += [[0] * 12]
		for i in range(12):
			for j in range(12):
				matriz[i][j] = float(input())

		media = 0
		qnt = 0
		fim = 11
		for i in range(12):
			for j in range(12):
				if j > fim:
					media += matriz[i][j]
					qnt += 1
			fim -= 1
			
		media /= qnt
		print('%.1f' %media)

if __name__ == '__main__':
	main()