def main():
	#Entrada
	num1 , num2, num3, num4= input().split()
	n1 = float(num1)
	n2 = float(num2)
	n3 = float(num3)
	n4 = float(num4)
		#n = nota
	#Processamento
		#p = peso
	p1, p2, p3, p4 = 2, 3, 4, 1
	media = (n1*p1 + n2*p2 + n3*p3 + n4*p4) / (p1+p2+p3+p4)
	print('Media: %.1f' %media)
	if media >= 7:
		print('Aluno aprovado.')
	elif media < 5:
		print('Aluno reprovado.')
	elif media >=5 and media <=6.9:
		print('Aluno em exame.')
		nota_exame = float(input())
		print('Nota do exame: %.1f' %nota_exame)
		media_exame = (media + nota_exame) /2
		if media_exame >= 5:
			print('Aluno aprovado.')
		else:
			print('Aluno reprovado.')
		print('Media final: %.1f' %media_exame)


if __name__ == '__main__':
	main()