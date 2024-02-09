 # Programa para calcular el area y el perimetro de un circulode radio R

import math

# input
R = input("ingrese el valor del radio del circulo")
R = int(R)

# processing
A = math.pi*R*R
P = 2*math.pi*R


# output
print("el area del circulo es: " + str(A))
print("el perimetro del circulo es: " + str(P))