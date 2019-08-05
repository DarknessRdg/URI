def main():
	
	contador = 1
	postividade = 0

	while contador <= 6:
		num = float(input())
		contador += 1
		if num > 0:
			postividade += 1
		else:
			postividade = postividade

	print(postividade,'valores positivos')


if __name__ == '__main__':
	main()