valores1 = input()
ponto1 = valores1.split()
x1 = float(ponto1[0])
y1 = float(ponto1[1])

valores2 = input()
ponto2 = valores2.split()
x2 = float(ponto2[0])
y2 = float(ponto2[1])

distancia1 = ((x2-x1)**2  +  (y2-y1)**2)**(1/2)  
print('%.4f' %distancia1)