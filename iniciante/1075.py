def main():
	num = int(input())

	contador = 1
	while  contador <= 10000:
		if (contador % num) == 2:
			print(contador)
		contador +=1

if __name__ == '__main__':
	main()