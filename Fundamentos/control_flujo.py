

# Condicionales =================================

# if
comando = "Otra cosa"
if comando == "entrar":
	pass
elif comando == "saludar":
	pass
elif comando == "salir":
	pass
else:
	pass

# Califiaciones 
# nota = float(input("Introduce tu nota: "))
nota = 9
if nota >= 9:
	print("Sobresaliente")
if nota >= 7 and nota < 9:
	print("Notable")
if nota >= 6 and nota < 7:
	print("Bien")
if nota >= 5 and nota < 6:
	print("Suficiente, justo")
if nota < 5:
	print("Reprobaste")

# El pass nos puede servir para hacer una estructura, un esqueleto

print()

# Iterativas =================================

# While
c = 0
while c <= 5:
	c+=1
	if c == 4:
		print("Rompemos el bucle cuando c vale",c)
		break
	print("c vale",c)
else:
	print("Se ha completado toda la iteracion y c vale", c)

print()

c = 0
while c <= 5:
	c+=1
	if c == 4:
		print("Continuamos con la siguiente iteracion",c)
		continue
	print("c vale",c)
else:
	print("Se ha completado toda la iteracion y c vale", c)

print()

# Menu interactivo
print("Bienvenido al menu interactivo")
while (True):
	print("""¿Que quieres hacer? Escriba una opcion:
	1) Saludar
	2) Sumar dos numeros
	3) Salir""")

	opcion = int(input())

	if opcion == 1:
		print("Hola este es un saludo, todo bien?")
	elif opcion == 2:
		n1 = float(input("Introduce el primer numero: "))
		n2 = float(input("Introduce el segundo numero: "))
		print("El resultado es la suma es: ", n1+n2)
	elif opcion == 3:
		print("Hasta luego, saludos")
		break
	else:
		print("El comando es desconocido, intentalo otra ves")
	
print()

# For
indice = 0
numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
	numeros[indice] *= 10
	indice+=1
print(numeros)

print()

for i in range(10):
	print(i)