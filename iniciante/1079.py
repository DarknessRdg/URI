def main():
	num_de_vezes = int(input())

	contador = 1
	while  contador <= num_de_vezes:
		num1, num2, num3 = input().split()
		num1 = float(num1)
		num2 = float(num2)
		num3 = float(num3)

		media = (num1*2 + num2*3 + num3*5) / (2+3+5)

		print("%.1f" %media)
		contador +=1

if __name__ == '__main__':
	main()