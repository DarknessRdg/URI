def main():
	while True:
		try:
			frase = input().lower()
			new_line = ''

			cont = 0 
			for letra in frase:
				if ord(letra) >=  97 and ord(letra) <= 122:
					if cont%2 == 0:
						new_line += letra.upper()
						cont += 1
					else:
						new_line += letra.lower()
						cont += 1
				else:
					new_line += letra
			print(new_line)
		except:
			break

if __name__ == '__main__':
	main()