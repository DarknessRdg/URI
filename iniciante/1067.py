def main():
	
	num = int(input())
	
	quantidade_repetições = 1

	while quantidade_repetições <= num:	
		if (quantidade_repetições % 2) != 0:
			print(quantidade_repetições)

		quantidade_repetições += 1

	
	
if __name__ == '__main__':
	main()