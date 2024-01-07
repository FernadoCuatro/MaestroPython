# Para trabajr con ficheros debe importarse:
from io import open

# Hacemos el proceso
texto = "Una linea con texto\nOtra linea sin texto"

# Creamos un fichero
# Y abrimos un fichero
# 1. Nombre del archivo
# 2. El modo de abrir, en este caso W es en escritura
# fichero = open("fichero.txt", "w")

# Escribimos en este fichero
# fichero.write(texto)

# Cerramos el fichero
# fichero.close()

# Para borrar un fichero
# del(fichero)


# Abrir fichero en modo lectura
# r = read
fichero_lec = open("fichero.txt", "r")
# Guardamos en una variable el contenido de todo el fichero
# texto_lec = fichero_lec.read()
# Guardar informacion en una lista
lineas = fichero_lec.readlines()

fichero_lec.close()
# print(texto_lec)

# print(lineas)
print(lineas[0])

# Agregar una linea al final
# a = append
fichero_edit = open("fichero.txt", "a")
fichero_edit.write("\nCuarta Linea del fichero")
fichero_edit.close()

print(lineas[-1])

# No se puede abrir un archivo en modo r/read/lectura si no existe
# con el a/append/Añadir si se crea el archivo es como
# el w/write/escribir, que tambien lo crea

# Leer el contenido poco a poco, lina por linea
fichero = open("fichero.txt", "r")
l = fichero.readline()
# Cada ves que se ejecuta, el puntero cambia de linea
fichero.close()

# Leer linea secuencial, automatizada
with open("fichero.txt", "r") as fichero:
	for lineas in fichero:
		print(lineas)

fichero.close()