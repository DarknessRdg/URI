def main():
	#ENTRADA
	num1, num2, num3, num4 = input().split()
	a = int(num1)
	b = int(num2)
	c = int(num3)
	d = int(num4)
	#PRECESSAMENTO
	if b>c and d>a  and (c+d)>(a+b) and (c>0 and d>0) and ( (a%2) == 0):
		print('Valores aceitos')
	else:
		print('Valores nao aceitos')	

if __name__ == '__main__':
	main()