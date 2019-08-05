def main():
	#Entrada
	x = int(input())
	y = int(input())

	somador = 0
	#processamento
	if x > y :
		for i in range(y, x+1):
			if i%13 !=0:
				somador += i
	else:
		for i in range(x, y+1):
			if i%13 !=0:
				somador += i
	print(somador)


if __name__ == '__main__':
	main()