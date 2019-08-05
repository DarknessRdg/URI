def main():
	#Entrada	
	num1 = int(input()) 
	num2 = int(input())
	#Processamento
	maior, menor = ordem_crescente(num1,num2)
	soma = 0

	if menor >0 :
		while menor < maior:
			if (menor % 2) != 0:
				soma += menor

			menor = menor + 1
	else:
		while  menor < maior:
			menor +=1
			if (menor % 2) != 0:
				soma += menor	

	#Saida
	print(soma) 
		

	
def ordem_crescente(a,b):
	if a>b:
		maior = a 
		menor = b
	else:
		maior = b
		menor = a
	return maior, menor

if __name__ == '__main__':
	main()