def main():
	# (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim)
	# Caso o usuário informe um código inválido deve ser solicitado um novo código 
	# O programa será encerrado quando o código informado for o número 4.

	#Contadores
	alcool = 0
	gasolina = 0
	diesel = 0

	#Porcessamento
	while True:
		#Entrada
		cod = int(input())

		#Processamento
		if cod == 1:
			alcool +=1
		elif cod == 2:
			gasolina +=1
		elif cod == 3:
			diesel +=1
		
		#Saida
		elif cod == 4:
			print('MUITO OBRIGADO')
			print('Alcool:',alcool)
			print('Gasolina:', gasolina)
			print('Diesel:',diesel)
			break 

if __name__ == '__main__':
	main()