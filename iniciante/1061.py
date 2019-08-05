def main():
	#Entrada
		#INICIO
	data1, num1 = input().split()
	dia1 = int(num1)
	tempo1, tempo2, tempo3 = input().split(' : ')
	hora_inicio , min_inicio , seg_inicio = tranformar_tempo(tempo1,tempo2,tempo3)
		#FIM
	data2, num2 = input().split()
	dia2 = int(num2)
	tempo4, tempo5, tempo6 = input().split(' : ')
	hora_fim, min_fim, seg_fim = tranformar_tempo(tempo4,tempo5,tempo6)
	#Processamento

	tempo_s1 = dia1*24*60*60 + hora_inicio*60*60+ min_inicio*60 +seg_inicio
	tempo_s2 = dia2*24*60*60 + hora_fim*60*60+ min_fim*60 +seg_fim

	quantidade = tempo_s2 - tempo_s1


	dias = quantidade//86400
	horas = (quantidade%86400)//3600
	minutos = ((quantidade%86400) %3600) //60
	segundos = ((quantidade %86400)%3600)%60

	
	print(dias, 'dia(s)')
	print(horas,'hora(s)')
	print(minutos,'minuto(s)')
	print(segundos,'segundo(s)')

def tranformar_tempo(a,b,c):
	horas = int(a)
	minutos = int(b)
	segundos = int(c)
	return horas,minutos,segundos
def delta(a,b):
	if a>=b:
		delta = a-b
	else:
		delta = b-a
	return delta


if __name__ == '__main__':
	main()