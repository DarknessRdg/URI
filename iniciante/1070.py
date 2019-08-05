def main():
	
	num = int(input())
	
	contador_impares = 0

	while contador_impares < 6:
		if (num % 2) != 0:
			print(num)
			contador_impares += 1
		num += 1
		

	
	
if __name__ == '__main__':
	main()