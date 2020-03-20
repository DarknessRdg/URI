def eh_perfeito(n):
  soma = 0
  for i in range(n - 1, 0, -1):
    if n % i == 0:
      soma += i

  return n == soma


if __name__ == '__main__':
  for i in range(int(input())):
    n = int(input())
    if eh_perfeito(n):
      print(n, 'eh perfeito')
    else:
      print(n, 'nao eh perfeito')
