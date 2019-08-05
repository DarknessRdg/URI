def main():
	qnt = int(input())
	for i in range(qnt):
		linha = input()
		tamanho = len(linha)
		metade = tamanho//2
		new_line = ''
		#1º Problema
		for i in range(tamanho):
			tabelaASC = ord(linha[i])

			if (tabelaASC >= 65 and tabelaASC <= 90) or (tabelaASC >= 97 and tabelaASC <=122):
				letra_nova = chr(tabelaASC + 3)
				new_line += letra_nova
			else:
				new_line += linha[i] 
		#2º Problema
		new_line = new_line[::-1]
		#3º Problema
		metade_pra_frente = new_line[metade:]
		new_line = new_line[:metade]
		
		for i in range(len(metade_pra_frente)):
			tabelaASC = ord(metade_pra_frente[i])
			new_line += chr(tabelaASC-1)	
		#Saida
		print(new_line)


if __name__ == '__main__':
	main()