def main():
	qnt = int(input())

	for i in range(qnt):
		lista_padrao = list(input())

		qnt_sequencias = int(input())
		for j in range(qnt_sequencias):
			sequencia = list(input())
			
			if verificar_sequencia(lista_padrao, sequencia):
				print('Yes')
			else:
				print('No')

def verificar_sequencia(conjunto, sequencia):
	cont = 0
	indice = 0
	for i in range(cont, len(sequencia)):
		for j in range(indice, len(conjunto)):
			if sequencia[i] == conjunto[j]:
				cont += 1
				indice = j + 1
				break
	if cont == len(sequencia):
		return True
	else:
		return False
				


if __name__ == '__main__':
	main()