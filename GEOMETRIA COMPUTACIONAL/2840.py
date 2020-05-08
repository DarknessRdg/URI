pi = 3.1415

r, l = map(int, input().split())
volume = (4/3) * (pi * r**3)


print(int(l // volume))
