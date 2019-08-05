# ord('a') = 97 
# chr('97') = 'a'
def main():
	qnt = int(input())
	for i in range(qnt):
		a, b = input().split()

		if b in a:
			print('encaixa')
		else:
			print('nao encaixa')


if __name__ == '__main__':
	main()