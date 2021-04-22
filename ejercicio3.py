"""Escribe un programa en Python que acepte una cadena de caracteres y cuente el tamaño de la 
cadena y cuantas veces aparece la letra A (mayuscula y minúscula)"""

print("Ingrese una cadena de caracteres")
cadena= input()
cantidad_caracteres=len(cadena)
total_a=cadena.count('a')#+cadena.count('A')

print("El tamaño de la cadena ingresa es: " +str(cantidad_caracteres)+ " la letra A se repite : "+ str(total_a)+" veces")