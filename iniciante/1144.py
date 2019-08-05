def main():
	n = int(input())

	for i in range(1,n+1):
		num1 = i
		num2 = i**2
		num3 = num1 * num2
		print(num1, num2, num3)
		print(num1, num2+1, num3+1)
		
if __name__ == '__main__':
	main()