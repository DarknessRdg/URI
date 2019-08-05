def main():
	qnt_casos_teste = int(input())
	for i in range(qnt_casos_teste):
		lista_produto = []
		lista_preço = []

		qnt_produto = int(input())
		for j in range(qnt_produto):
			produto_, preço_ = input().split()
			lista_produto += [produto_]
			lista_preço += [float(preço_)]

		qnt_compra = int(input())
		total_compra = 0
		for i in range(qnt_compra):
			produto_ , quantidade = input().split()
			indice = encontrar_produto(lista_produto, produto_)
			
			total_compra += lista_preço[indice] * int(quantidade)
		
		print('R$ %.2f' %total_compra)

def encontrar_produto(lista_produto, produto):
	for i in range(len(lista_produto)):
		if lista_produto[i] == produto:
			return i
	
	return -1			

if __name__ == '__main__':
	main()