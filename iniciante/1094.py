def main():
	#Entrada
	contador = 0
	limitador = int(input())

	sapo = 0
	rato = 0
	coelho = 0
	
	#Processamento
	while  contador < limitador:
		quantidade, categoria = input().split()
		quantidade = int(quantidade)
		contador += 1

		if categoria == 'S':
			sapo += quantidade

		elif categoria == 'R':
			rato += quantidade

		elif categoria == 'C':
			coelho += quantidade

	total = sapo + rato + coelho
	porcento_sapo = sapo / total
	porcento_rato = rato / total
	porcento_coelho = coelho / total	

	#Saida
	print('Total:',total,'cobaias')
	print('Total de coelhos:',coelho)
	print('Total de ratos:',rato)
	print('Total de sapos:',sapo)

	print('Percentual de coelhos: %.2f %%' %(porcento_coelho*100))
	print('Percentual de ratos: %.2f %%' %(porcento_rato*100))
	print('Percentual de sapos: %.2f %%' %(porcento_sapo*100))

if __name__ == '__main__':
	main()