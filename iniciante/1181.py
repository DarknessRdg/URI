def main():
	linha = int(input())
	operaçao = input()

	matriz = []
	for i in range(12):
		matriz += [[0] * 12]
	for i in range(12):
		for j in range(12):
			matriz[i][j] = float(input())

	soma = 0
	for i in range(12):
		for j in range(12):
			if i == linha:
				soma += matriz[i][j]

	if operaçao == 'S':
		print('%.1f' %soma)
	else:
		print('%.1f' %(soma/12))



if __name__ == '__main__':
	main()