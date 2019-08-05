def main():
	while True:
		try:
			linha = input()
			new_line = ''
			for letra in linha:
				valor_letra = ord(letra)
				
				if valor_letra >= 97 and valor_letra <= 122:
					valor_letra += 13
					if valor_letra > 122:
						valor_letra = (valor_letra - 122) + 96
						new_line += chr(valor_letra)
					else:
						new_line += chr(valor_letra)
				
				elif valor_letra >= 65 and valor_letra <= 90:
					valor_letra += 13
					if valor_letra > 90:
						valor_letra = (valor_letra - 90) + 64
						new_line += chr(valor_letra)
					else:
						new_line += chr(valor_letra)
				else:
					new_line += letra

			print(new_line)
		except:
			break


if __name__ == '__main__':
	main()