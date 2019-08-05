def main():
	
	quantidade_repetições = 1 
	contador_pares = 0

	while quantidade_repetições <= 5:
		num = int(input())
		quantidade_repetições += 1

		if num %2 == 0:
			contador_pares +=1
		else:
			contador_pares = contador_pares 

	print(contador_pares,'valores pares')

if __name__ == '__main__':
	main()