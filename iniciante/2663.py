def main():
	qnt = int(input())
	minimo_aprovados = int(input())

	lista_de_notas = []
	for i in range(qnt):
		lista_de_notas.append(int(input()))

	lista_de_notas.sort(reverse=True)

	a_mais = qnd_a_mais(lista_de_notas, minimo_aprovados)
	print(minimo_aprovados + a_mais)

def qnd_a_mais(lista, qnt_aprovados):
	a_mais = 0
	for i in range(qnt_aprovados - 1 , len(lista) - 1):
		if lista[i] == lista[i + 1]:
			a_mais += 1
		else:
			return a_mais
	return a_mais
	


if __name__ == '__main__':
	main()