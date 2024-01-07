# Todo esto es muy basico mister, ya lo sabemos. 

print("Suma de: " + str(2 + 7))

print()

print("El salto de linea\nY la tabulacion\tde toda la vida jajaja")

print()

# Para manejar los directorios
print(r"C/local/usuario/nombre")

print()

# Manejar varias lineas en un solo print
print("""Una linea
con un salto normal
y con\notro salto pero con la n""")

print()

# Indices de las cadenas
palabra = "python"
print(palabra[0])

# Sustraer de una palbra
print(palabra[0:3])
print(palabra[3:])
print(palabra[-2:])

# Cambiar una letra de una palabra
palabra = "N" + palabra[1:]
print(palabra)

# Cuantos caracteres tiene
print(len(palabra))

print()

# Listas
numeros = [1,2,3,4,5,"Fernando",-3]

print(numeros[-2:])
numeros[0] = 0
print(numeros)

# Añadir al final
numeros.append(15)
print(numeros)

#Asignar con slasing
letras = ['a', 'b', 'c', 'd', 'e', 'f']
print(letras[:3])
letras[:3] = ['A','B','C']
print(letras)
letras[:1] = ['B','C']
print(letras)
print(len(letras))

# Se pueden tener listas anidadas tranquilamente 

print()

# Hacemos el ejemplo de los numeros pares o impares
n = 0
while n<=10:
	if (n%2)==0:
		print(n,' es un numero par')
	else:
		print(n,' es un numero impar')
	n = n + 1

print()

# Leer datos del teclado
valor = input("Escriba algo: ")
valor = float(valor)
valor = float(input("Escriba algo mas: "))
print(valor)