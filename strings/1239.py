def main():
	while True:
		try:		
			linha = input()
			contador_astericos = 0
			contador_underline = 0

			nova = ''
			for i in linha:
				if i == '_':
					if contador_underline%2 == 0:
						nova += '<i>'
						contador_underline +=1
					else:
						nova += '</i>'
						contador_underline +=1
				elif i == '*':
					if contador_astericos%2 == 0:
						nova += '<b>'
						contador_astericos +=1
					else:
						nova += '</b>'
						contador_astericos +=1
				else:
					nova += i
			print(nova)
		except:
			break

if __name__ == '__main__':
	main()