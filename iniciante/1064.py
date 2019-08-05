def main():

	contador = 0
	contadorPOSITIVO = 0
	somador = 0
	while contador <6:
		num = float(input())
		contador += 1
		if num>0:
			contadorPOSITIVO += 1
			somador = somador + num

	media = somador/contadorPOSITIVO 
	print(contadorPOSITIVO,'valores positivos')
	print('%.1f' %media)

if __name__ == '__main__':
	main()