def main():
	#entrada
	qnt = int(input())

	for i in range(qnt):
		letreiro = input()
		calculo_qnt_leds(letreiro)

#Funcoes
def calculo_qnt_leds(letreiro):
	valor = 0
	for z in range(len(letreiro)):
		if letreiro[z] == '1':
			valor += 2
		elif letreiro[z] == '2':
			valor += 5
		elif letreiro[z] == '3':
			valor += 5
		elif letreiro[z] == '4':
			valor += 4
		elif letreiro[z] == '5':
				valor += 5
		elif letreiro[z] == '6':
			valor += 6
		elif letreiro[z] == '7':
			valor += 3
		elif letreiro[z] == '8':
			valor += 7
		elif letreiro[z] == '9':
			valor += 6
		elif letreiro[z] == '0':
			valor += 6
	print(valor,'leds')
if __name__ == '__main__':
	main()