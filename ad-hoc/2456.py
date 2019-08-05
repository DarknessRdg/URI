def main():
	sequencia = input().split()
	for i in range(len(sequencia)):
		sequencia[i] = int(sequencia[i])

	if verificar_ordem_crescente(sequencia):
		print('C')
	elif verificar_ordem_decreescente(sequencia):
		print('D')
	else:
		print('N')

def verificar_ordem_crescente(lista):
	for i in range(1, len(lista)):
		if lista[i - 1] > lista[i]:
			return False
	return True

def verificar_ordem_decreescente(lista):
	for i in range(1, len(lista)):
		if lista[i - 1] < lista[i]:
			return False
	
	return True


if __name__ == '__main__':
	main()