def main():
	qnt = int(input())
	vetor = [0] * 1000

	valor = 0
	for i in range(1000):
		vetor[i] = valor
		print('N[%d] = %d' %(i, vetor[i]))
		valor += 1
	
		if valor == qnt:
			valor = 0


if __name__ == '__main__':
	main()