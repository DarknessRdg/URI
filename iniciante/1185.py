def main():
	operaçao = input()

	matriz = []
	for i in range(12):
		matriz += [[0] * 12]
	for i in range(12):
		for j in range(12):
			matriz[i][j] = float(input())
	
	soma = 0
	qnt = 0
	
	fim = 11
	for i in range(12):
		for j in range(12):
			if j < fim:
				soma += matriz[i][j]
				qnt += 1
		fim -= 1

	if operaçao == 'S':
		print('%.1f' %soma)
	else:
		print('%.1f' %(soma/qnt))


if __name__ == '__main__':
	main()