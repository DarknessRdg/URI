def main():
	vetor = [0] * 100
	vetor[0] = float(input())
	print('N[0] = %.4f' %vetor[0])
	
	for i in range(1, 100):
		vetor[i] = vetor[i - 1] / 2

		print('N[%d] = %.4f' %(i, vetor[i]))

if __name__ == '__main__':
	main()