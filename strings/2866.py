for j in range(int(input())):
  p = input()

  palavra = []
  for i in p:
    if 'a' <= i <= 'z':
      palavra.append(i)

  print(''.join(palavra)[::-1])
  
