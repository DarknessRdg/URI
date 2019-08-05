def main():
	letra_i = 1
	letra_j = 60

	while  letra_j >= 0:
		print('I=%d J=%d' %(letra_i,letra_j))

		letra_i += 3
		letra_j -=5

if __name__ == '__main__':
	main()