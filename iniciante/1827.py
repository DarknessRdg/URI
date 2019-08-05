def main():
	while True:
		try:
			ordem = input()
			if ordem == '':
				continue
			else:
				ordem = int(ordem)
				if ordem % 2 == 0:
					continue

			matriz = []
			for i in range(ordem):
				matriz += [[0] * ordem]

			valor_central = ordem//2

			diagonal_principal(matriz)
			diagonal_secundaria(matriz)
			recheio(matriz, ordem)
			central(matriz, valor_central)


			for i in range(ordem):
				for j in range(ordem):
					print(matriz[i][j], end='')
				print()
			print()

	
		except EOFError:
			break	


def diagonal_principal(matriz):
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if i == j:
				matriz[i][j] = 2


def diagonal_secundaria(matriz):
	fim  = len(matriz) - 1
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if j == fim:
				matriz[i][j] = 3
		fim -= 1

def central(matriz, centro):
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if i == centro and j == centro:
				matriz[i][j] = 4


def recheio(matriz, tamanho):
	meio = tamanho//3
	for i in range(meio, len(matriz) - meio):	
		for j in range(meio, len(matriz[i]) - meio):
			matriz[i][j] = 1
			


if __name__ == '__main__':
	main()