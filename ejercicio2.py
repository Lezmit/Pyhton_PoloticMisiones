"""Escribe un programa Python que acepte un número entero (n) y calcule el valor de n + nn + nnn"""

print("Ingrese número: ")
n=int(input())

valor=n+(n*10+n)+(n*100+n*10+n)
print("El valor de n+nn+nnn, es igual a: "+str(valor))

