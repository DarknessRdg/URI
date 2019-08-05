def main():
	valor = int(input())
	vetor = [valor] * 10
	print('N[0] = %d' %vetor[0])
	
	for i in range(1, 10):
		vetor[i] = vetor[i - 1] * 2
		print('N[%d] = %d' %(i, vetor[i]))


if __name__ == '__main__':
	main()