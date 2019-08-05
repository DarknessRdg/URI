def main():

	while  True:
		try:
			
			ordem = int(input())
			if ordem == 0:
			 	break
			matriz = []
			for i in range(ordem):
				matriz.append([1] * ordem)

			inicio = 1
			fim = ordem - 1
			valor = 2
			
			while fim - inicio > 0:
				
				for i in range(inicio, fim):
					for j in range(inicio, fim):
						matriz[i][j] = valor
				inicio += 1
				fim -= 1
				valor += 1
			for i in range(ordem):
				for j in range(ordem):
					matriz[i][j] = str(matriz[i][j])
					tamanho = len(matriz[i][j])
					if j == 0:
						if tamanho == 1:
							print('  ' + matriz[i][j], end='')
						elif tamanho == 2:
							print(' ' + matriz[i][j], end='')
						else:
							print(matriz[i][j], end='')
					else:
						if tamanho == 1:
							print('   ' + matriz[i][j], end='')
						elif tamanho == 2:
							print('  ' + matriz[i][j], end='')
						else:
							print(' ' + matriz[i][j], end='')
				print()
			print()

		except:
			break


if __name__ == '__main__':
	main()
