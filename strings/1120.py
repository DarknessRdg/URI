def main():
	while  True:
		n, m = input().split()

		if n == '0' and m == '0':
			break
		
		else:
			for i in range(len(m)):
				m = m.replace(n,'')

			if m == '':
				m = 0
				print(m)
		
			elif m.isalnum():
				m = int(m)
				print(m)
			
			else:
				print(m)		

if __name__ == '__main__':
	main()
  
