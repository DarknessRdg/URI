def main():
	qnt = int(input())
	for k in range(qnt):
		contador_print = 0

		num_alunos = int(input())
		alunos = input().split()
		presenças = input().split()

		for i in range(len(alunos)):
			presença_aluno = 0
			ausencia = 0
			qnt_aula = 0
			for j in presenças[i]:
				if j == 'P':
					presença_aluno += 1
				elif j == 'A':
					ausencia += 1
				elif j == 'M':
					continue

				qnt_aula +=1
			if qnt_aula == 0:
				media = 100	
			else:
				media = (presença_aluno/qnt_aula) * 100

			if media < 75:
				contador_print += 1
				if contador_print == 1:
					print(alunos[i], end='')
				else:
					print('', alunos[i], end='')

		print()

				
if __name__ == '__main__':
	main()