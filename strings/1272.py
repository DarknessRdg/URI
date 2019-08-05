def main():
	qnt = int(input())
	for i in range(qnt):
		texto = input().split()
		for j in texto:
			print(j[0], end= '')
		print()


if __name__ == '__main__':
	main()