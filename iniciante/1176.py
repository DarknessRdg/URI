def main():
	qnt  = int(input())
	for i in range(qnt):

		n = int(input())
	
		sequencia = fibonacci(n)
		print('Fib(%d) = %d' %(n, sequencia[n]))

def fibonacci(n):
	sequencia = [0,1]
	
	if n > 1:
		for i in range(1,n):
			sequencia += [sequencia[i-1] + sequencia[i]]

	return sequencia



if __name__ == '__main__':
	main()