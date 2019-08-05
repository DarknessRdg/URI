def main():
	#Entrada
	num1, num2 = input().split()
	cod1 = int(num1)
	quantidade = int(num2)
	#Processamento
		#preço cod1:
	if cod1 == 1 :
		valor1 = 4
	elif cod1 == 2:
		valor1 = 4.50
	elif cod1 == 3:
		valor1 = 5
	elif cod1 == 4:
		valor1 = 2
	elif cod1 == 5:
		valor1 = 1.50
		
	valor_pago = valor1 * quantidade
	#saida
	print('Total: R$ %.2f' %valor_pago)

if __name__ == '__main__':
	main()