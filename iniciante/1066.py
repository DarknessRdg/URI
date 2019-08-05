def main():
	
	quantidade_repetições = 1 
	
	contador_pares = 0
	contador_impares = 0
	contador_positivos = 0
	contador_negativos = 0

	while quantidade_repetições <= 5:
		num = int(input())
		quantidade_repetições += 1

		if num %2 == 0:
			contador_pares +=1
		else:
			contador_impares += 1

		if num > 0:
			contador_positivos += 1
		elif num < 0:
			contador_negativos +=1 

	print(contador_pares,'valor(es) par(es)')
	print(contador_impares,'valor(es) impar(es)')
	print(contador_positivos, 'valor(es) positivo(s)')
	print(contador_negativos,'valor(es) negativo(s)')

if __name__ == '__main__':
	main()