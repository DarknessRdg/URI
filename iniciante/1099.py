def main():
	n = int(input())
	
	for i in range(n):
		x,y = map(int, input().split())		
		contador = 0
		if x < y:
			x +=1
			while x < y:
				if (x %2) == 0:
					contador = contador
				else:
					contador += x
				x +=1
			print(contador) 
		else:
			y +=1
			while y < x:
				if (y %2) == 0:
					contador = contador
				else:
					contador += y
				y +=1
			print(contador)	


if __name__ == '__main__':
	main()