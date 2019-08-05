def main():
	vetor_par = []
	vetor_impar = []
	for i in range(15):
		numero = int(input())

		if numero % 2 == 0:
			vetor_par += [numero]
		else:
			vetor_impar += [numero]

		if len(vetor_impar) == 5:
			for i in range(5):
				print('impar[%d] = %d' %(i, vetor_impar[i]))
			vetor_impar = []
		if len(vetor_par) == 5:
			for i in range(5):
				print('par[%d] = %d' %(i, vetor_par[i]))
			vetor_par = []

	if  len(vetor_impar) > 0:
		for i in range(len(vetor_impar)):
			print('impar[%d] = %d' %(i, vetor_impar[i]))
	if len(vetor_par) > 0:
		for i in range(len(vetor_par)):
			print('par[%d] = %d' %(i, vetor_par[i]))

if __name__ == '__main__':
	main()