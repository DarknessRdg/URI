def main():
	qnt = int(input())
	for cont in range(qnt):
		ordem = int(input())

		matriz = []
		for i in range(ordem):
			valores = list(map(int, input().split()))

			matriz.append(valores)
		
		# Ja fazendo o quadrado e transformando pra str, pra trabalhar mais facil
		for i in range(ordem):
			for j in range(ordem):
				matriz[i][j] = str(matriz[i][j] ** 2)
		
		# Adicionando os espaços necessários
		matriz_de_colunas = [] 
		for i in range(ordem):
			conluna = []
			for j in range(ordem):
				conluna.append(matriz[j][i])
			
			tamanho = maior(conluna)
			adicionar_espaço(conluna, ordem, tamanho)
			matriz_de_colunas.append(conluna)
		
		# Colocando os numeros com espaços na matriz
		
		for i in range(ordem):
			for j in range(ordem):
				matriz[i][j] = matriz_de_colunas[j][i]
		

		#Print
		print('Quadrado da matriz #%d:' %(4 + cont))
		for i in range(ordem):
			for j in range(ordem):
				if j == ordem - 1 :
					print(matriz[i][j], end='')
				else:	
					print(matriz[i][j], end=' ')
			print()
		if cont  != qnt - 1:
			print()
		


def maior(lista):
	maior = len(lista[0])
	for i in range(1, len(lista)):
		if len(lista[i]) > maior:
			maior = len(lista[i]) 
	return maior




def adicionar_espaço(lista, ordem, tamanho):
	for i in range(ordem):
		lista[i] = (' ' * (tamanho - len(lista[i])) ) + lista[i] 
	return 



		
if __name__ == '__main__':
	main()