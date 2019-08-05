def main():
	while True:
		
		m,n = map(int, input().split())	
		somador = 0
		if m <= 0 or n <= 0:
			break

		elif n < m:
			while n <= m:
				print(n, end=' ')
				somador += n
				n +=1
		
			print('Sum=%d'%somador)
		else:
			while m <= n:
				print(m, end=' ')
				somador += m
				m +=1
		
			print('Sum=%d'%somador)




if __name__ == '__main__':
	main()