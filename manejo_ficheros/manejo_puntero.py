# Para trabajr con ficheros debe importarse:
from io import open

fichero = open("fichero.txt","r")

# Quitamos el puntero del inicio 
# Y lo colocamos en el caracter 10
fichero.seek(10)

# Al hacer un read, se empieza a leer el archivo
# desde la posicion 10, es decir, donde apunta el puntero

# Despues de read(), despues de leer el contenido
# El puntero se va al final

# Esto tambien se puede hacer con un read
# fichero.read(5)

# r+ => Lectura y escritura 

# Modificar linea despues de leer
# lineas[2] = "Esta linea se ha modificado en memoria\n"

# Escribir una serie de linea de texto
# Recibe una lista 
# fichero.writelines(lineas)