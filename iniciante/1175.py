def main():
	vetor = []
	for i in range(20):
		vetor += [int(input())]

	primeiro = 0
	ultimo = len(vetor) - 1
	for i in range(10):
		menor = vetor[primeiro]
		maior = vetor[ultimo]
		vetor[primeiro] = maior
		vetor[ultimo] = menor

		primeiro += 1
		ultimo -= 1
	
	for i in range(len(vetor)):
		print('N[%d] = %d' %(i, vetor[i]))


if __name__ == '__main__':
	main()




