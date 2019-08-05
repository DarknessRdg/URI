def main():
	engig = input().upper()
	palavra = input().upper()
	qnt = 0

	while True:
		try:
			if verificar	(engig, palavra):
				qnt += 1
			engig = engig[1:]

		except:
			break

	print(qnt)

def verificar(a,b):
	for i in range(len(b)):
		if a[i] == b[i]:
			return False
	return True


if __name__ == '__main__':
	main()