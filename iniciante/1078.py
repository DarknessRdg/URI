def main():
	num = int(input())

	contador = 1
	while  contador <= 10:
		x = contador * num 
		print(contador,'x',num,'=',x)

		contador +=1

if __name__ == '__main__':
	main()