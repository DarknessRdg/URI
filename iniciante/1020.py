def main():
	#Entrada
	idade = int(input())
	#Processamento
	anos = idade // 365
	meses = (idade%365)//30
	dias = (idade%365)%30
	#Saída
	print(anos, 'ano(s)')
	print(meses, 'mes(es)')
	print(dias, 'dia(s)')
if __name__ == '__main__':
	main()