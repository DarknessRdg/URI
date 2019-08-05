def main():

	x1, y1, x2, y2 = map(int, input().split())

	while x1 != 0 and y1 != 0  and x2 != 0 and y2 != 0:

		if ta_no_mesmo_lugar(x1, y1, x2, y2):
			print('0')
		elif ta_na_mesma_linha(x1, x2) or ta_na_mesma_coluna(y1, y2) \
			or ta_na_mesma_diagonal_01(x1, y1, x2, y2) or ta_na_mesma_diagonal_02(x1, y1, x2, y2):
			print('1')
		else:
			print('2')

		x1, y1, x2, y2 = map(int, input().split())



def ta_no_mesmo_lugar(x1, y1, x2, y2):
	return x1 == x2 and y1 == y2


def ta_na_mesma_linha(x1, x2):
	return x1 == x2


def ta_na_mesma_coluna(y1, y2):
	return y1 == y2


def ta_na_mesma_diagonal_01(x1, y1, x2, y2):
	return x1 - y1 == x2 - y2 


def ta_na_mesma_diagonal_02(x1, y1, x2, y2):
	return x1 + y1 == x2 + y2


if __name__ == '__main__':
	main()