import sys

# Input para entrada pero debemos convertir los datos
dec = float(input("Introduzca un numero decimal con punto: "))

print()

valores = []
print("Introduce 3 valores")
for x in range(3):
	valores.append(input("Introduce el valor > "))

print(valores)