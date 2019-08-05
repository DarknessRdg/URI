def main():
	#Entrada
	num = float(input(""))
	#Processamento
	if 0 <= num and num <= 25:
		print("Intervalo [0,25]")
	elif  25 < num and num <= 50:
		print("Intervalo (25,50]")
	elif 50 < num and num <=75:
		print("Intervalo (50,75]")
	elif 75 < num and num <= 100:
		print("Intervalo (75,100]")
	elif 0>num or num>100:
		print("Fora de intervalo")
	
if __name__ == '__main__':
	main()