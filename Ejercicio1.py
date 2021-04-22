"""1. Escribe un programa Python que acepte el radio de un círculo del usuario y calcule el área. """
import math
print("Calcular Área de círculo")
print("Ingrese radio de circulo")
r = int(input())
a=math.pi*math.pow(r,2)

print("El área del círculo es: "+ str(round(a,2)))
