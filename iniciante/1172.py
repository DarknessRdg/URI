def main():
	vetor = []
	for i in range(10):
		vetor += [int(input())]

	for i in range(10):
		if vetor[i] <= 0:
			vetor[i] = 1
		print('X[%d] = %d' %(i,vetor[i]))


if __name__ == '__main__':
	main()