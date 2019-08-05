def main():
	volta = 0
	while True:
		try:
			volta += 1
			
			#Entrada
			ano = int(input())

			cont_bissexto = 0
			cont_hulu = 0
			cont_buku = 0

			#Processamento
			if volta > 2:
				print()
			
			if ano_bissexto(ano):
				print('This is leap year.')
				cont_bissexto += 1

			if huluculu(ano):
				print('This is huluculu festival year.')
				cont_hulu += 1
				
			if ano_bissexto(ano) and bulukulu(ano):
				print('This is bulukulu festival year.')
				cont_buku += 1
			
			if ano_bissexto(ano) == False and huluculu(ano) == False:
				print('This is an ordinary year.')

			if volta == 1 :
				print()
			

		except EOFError:
			break


def ano_bissexto(ano):
	if ano % 4 == 0 and ano % 400 == 0:
		return True
	elif ano % 4 == 0 and ano % 100 != 0:
		return True
	else:
		return False


def huluculu(ano):
	if ano % 15 == 0:
		return True
	else:
		return False


def bulukulu(ano):
	if ano % 55 == 0:
		return True
	else:
		return False


if __name__ == '__main__':
	main()