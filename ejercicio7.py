"""Escribe un programa en Python que reciba 5 números enteros del usuario y los guarde en una lista.
Luego recorrer la lista y mostrar los números por pantalla. """
lista=[]
for i in range(1,6):
    print("Ingrese numero:")
    n=int(input())
    lista.append(n)

print("La lista de numeros ingresados es: ")
for i in lista:
    print(i)
