def main():
	qnt = int(input())
	for z in range(qnt):
		frase = input().lower()
		alfabeto = 'abcdefghijklmnopqrstuvwxyz'
		#variaves
		contador_maior = 0
		indice_letra = ''
		#processamento
		for i in alfabeto:
			contador_freqnc = 0
			for j in frase:
				if i == j:
					contador_freqnc +=1
			if contador_freqnc == contador_maior:
				indice_letra += i
			elif contador_freqnc > contador_maior:
				indice_letra = i
				contador_maior = contador_freqnc

		for i in range(len(indice_letra)):
			print(indice_letra[i],end='')
		print()


if __name__ == '__main__':
	main()
