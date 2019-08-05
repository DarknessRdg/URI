valores = input()
splitados = valores.split()
a = float(splitados[0])
b = float(splitados[1])
c = float(splitados[2])
#TRIANGULO
triangulo = (a * c) / 2
#CIRCULO
pi = 3.14159
circulo = pi * c**2
#TRAPEZIO
trapezio = ((a + b)*c)/2
#QUADRADO
quadrado = b**2
#RETANGULO
retangulo  = a * b 
print('TRIANGULO: %.3f' %triangulo)
print('CIRCULO: %.3f' %circulo)
print('TRAPEZIO: %.3f' %trapezio) 
print('QUADRADO: %.3f' %quadrado) 
print('RETANGULO: %.3f' %retangulo)