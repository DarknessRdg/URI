def main():
	qnt = int(input())
	
	for i in range(qnt):
		a, b = input().split()

		new_line = ''
		resto = ''

		if len(a) > len(b):
			resto = a[len(b):]
			a = a[:len(b)]
		else:
			resto = b[len(a):]
			b = b[:len(a)]

		for i in range(len(a)):
			new_line += a[i] + b[i]

		new_line += resto
		print(new_line)



if __name__ == '__main__':
	main()