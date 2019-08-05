def main():
	qnt = int(input())
	for i in range(qnt):
		frase_criptografada = input()
		qnt_deslocada = int(input())
		new_line = ''

		for letra in frase_criptografada:
			valor = ord(letra) - qnt_deslocada
			if valor < 65:
				new_line += chr(91 - (65 - valor))
			else:
				new_line += chr(valor)
		
		print(new_line)


if __name__ == '__main__':
	main()