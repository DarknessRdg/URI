def main():
	instancias = int(input())
	
	for i in range(instancias):
		num_palavras, num_linhas_musica = map(int, input().split())

		japones = []
		portugues = []

		for j in range(num_palavras):
			japones.append(input())
			portugues.append(input())
		
		musica = []
		for j in range(num_linhas_musica):
			musica.append(input().split())	


		for j in range(len(musica)):
			traduçao = ''
			for k in range(len(musica[j])):
				x = posiçao_da_tracuçao(japones, musica[j][k])
				
				#SAIDA
				if k == 0:
					qnt = 0
				else:
					qnt = 1

				if x == -1:
					traduçao += ' ' * qnt + musica[j][k]
				else:
					traduçao += ' ' * qnt + portugues[x]

			print(traduçao)
	
		print()


def posiçao_da_tracuçao(japones, palavra):
	for i in range(len(japones)):
		if japones[i] == palavra:
			return i
	return -1
	
	
if __name__ == '__main__':
	main()