def main():
	#ENTRADA
	num1, num2, num3, num4 = input().split()
	horasINICIO = int(num1)
	minutosINICIO = int(num2)
	horasFIM = int(num3)
	minutosFIM = int(num4)
	#PRECESSAMENTO
	tempo_INICIO = (horasINICIO*60)+minutosINICIO
	tempo_FIM = (horasFIM*60)+minutosFIM

	if horasINICIO < horasFIM:
		duracao = delta (tempo_INICIO, tempo_FIM)
		horas = duracao //60
		minutos = duracao%60
	elif horasINICIO > horasFIM:
		if minutosFIM >= minutosINICIO:
			horas = (24 - horasINICIO) + horasFIM
			minutos = minutosFIM - minutosINICIO
		else:
			horas = ((24 - horasINICIO) + horasFIM) -1 
			minutos = (60 + minutosFIM) - minutosINICIO
	elif horasFIM == horasINICIO:
		if minutosFIM == minutosINICIO:
			horas = 24
			minutos = 0
		elif minutosFIM > minutosINICIO:
			horas = 0
			minutos  = delta(minutosINICIO, minutosFIM)
		else:
			horas = 23
			minutos = (minutosFIM + 60) - minutosINICIO

	
	print('O JOGO DUROU', horas,'HORA(S) E', minutos,'MINUTO(S)')	
def delta(a,b):
	if a>b:
		delta = a - b
	else:
		delta = b-a
	return delta



if __name__ == '__main__':
	main()