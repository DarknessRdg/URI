def main():
	#ENTRADA
	num1, num2 = input().split()
	horasINICIO = int(num1)
	horasFIM = int(num2)
	#PRECESSAMENTO
	
	if horasINICIO < horasFIM:
		fim_total = horasFIM - horasINICIO
		print('O JOGO DUROU %d HORA(S)' %fim_total)
	elif horasINICIO == horasFIM:
		print('O JOGO DUROU 24 HORA(S)')
	else:
		fim_total = (24 - horasINICIO) + horasFIM
		print('O JOGO DUROU %d HORA(S)' %fim_total)

if __name__ == '__main__':
	main()