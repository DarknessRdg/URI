def main():
	qnt = int(input())
	for i in range(qnt):
		diamantes = input().split('.')

		diamantes = ''.join(diamantes)
		
		cont = 0
		while True:
			posicao = diamantes.find('<>')
			if posicao >= 0:
				cont += 1
				
				x = list(diamantes)
				x.pop(posicao)
				x.pop(posicao)
				
				diamantes = ''.join(x)

			else:
				break
		print(cont)
		

if __name__ == '__main__':
	main()