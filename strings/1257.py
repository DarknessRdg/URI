def main():
	#INICIO
	qnt_total = int(input())


	for w in range(qnt_total):
		alfabeto = 'abcdefghijklmnopqrstuvwxyz'

		#Quantidade de palavras pra fazer a soma
		qnt_loop = int(input())
		somador = 0

		#PROCESSAMENTO
		for i in range(qnt_loop):
			palavra = input()

			for j in range(len(palavra)):
					valor = ord(palavra[j]) - 65
					somador += valor + j + i
					
		#SAIDA 
		print(somador)

if __name__ == '__main__':
	main()
