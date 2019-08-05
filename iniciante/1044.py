def main():
	#Entrada
	num1, num2 = input().split()
	a = int(num1)
	b = int(num2)
	#Processamento:
	if a > b:
		multipos = a%b
	else:
		multipos = b%a
	#Saida
	if multipos == 0:
		print('Sao Multiplos')
	else:
		print('Nao sao Multiplos')
if __name__ == '__main__':
	main()