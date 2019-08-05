def main():
	qnt = int(input())
	vetor = list(map(int, input().split()))

	menor = vetor[0]
	posiçao = 0
	for i in range(1, len(vetor)):
		if menor > vetor[i]:
			menor = vetor[i]
			posiçao = i
	print('Menor valor:', menor)
	print('Posicao:', posiçao)


if __name__ == '__main__':
	main()