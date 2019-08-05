def main():
	#Entrada
	num1, num2, num3 = input().split()
	n1 = int(num1)
	n2 = int(num2)
	n3 = int(num3)
	#Processamento:
	if n1 < n2 and n1 < n3:
		menor = n1
		if n2 < n3:
			meio = n2
			maior = n3
		else:
			meio = n3
			maior = n2
	elif n2 < n1 and n2 < n3:
		menor = n2
		if n1 < n3:
			meio = n1
			maior = n3
		else:
			meio = n3 
			maior = n1
	else:
		menor = n3
		if n1 < n2:
			meio = n1 
			maior = n2
		else:
			meio = n2 
			maior = n1

	#Saida
	print(menor)
	print(meio)
	print(maior)
	print()
	print(n1)
	print(n2)
	print(n3)


def main2():
    # uma outra forma menor utilizando as funcoes do python para ordenacao
    entrada = list(map(int, input().split()))
    ordenado = sorted(entrada)

    entrada, ordenado = '\n'.join(map(str, entrada)), '\n'.join(map(str, ordenado))

    print(ordenado + '\n')
    print(entrada)


if __name__ == '__main__':
	main()