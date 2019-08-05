def main():
	letra_i = 1
	letra_j = 7

	while  letra_i <= 9:
		print_3x(letra_i,letra_j)

		letra_i += 2
		letra_j += 2

def print_3x(a,b):
	print('I=%d J=%d' %(a,b))
	print('I=%d J=%d' %(a,(b -1)))
	print('I=%d J=%d' %(a,(b -2)))


if __name__ == '__main__':
	main()