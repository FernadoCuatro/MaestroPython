
lista = [1,2,3,4,5]

# añadir un elemento a una lista al final
lista.append(6)
print(lista)

# Limpiamos la lista, la dejamos vacia con el clear()

# unir varias listas con el l1.extends(l2)
# Se crea apartir de una lista nueva con esas dos 

# El count nos cuenta cuantas veces aparece una palabra
# .cout("Hola")

# index podemos buscar el indice donde aparece una 
# palabra en la lista .index("mundo")

# Agregar datos enmedio en una posicion en que noostros querramos
# Primero se pasa la posicion y despues el valor a tomar
# lista.insert[0,0]

# Con el .pop() sacamos un numero y lo eliminamos de la lista 
# Tambien se puede indicar con el indice
# .pop(0)

# Para eliminar directamente un valor
# Con el remove(30)
# Le pasamos el valor directamente


# Reverse nos permite darle la vuelta a una lista
# Y se revierte la propia lista

# Darle vuelta a una cadena por medio de una lista
lista_vuelta = list("Hola mundo")
# print(lista_vuelta)
lista_vuelta.reverse()
# Ahora convertimos en cadena
cadena = "".join(lista_vuelta)
print(cadena)

# Con la lista podemos ordenar los elementos
# Los ordenamos con el metodo sort()

# Para odenarlos al reves
# sort(reverse = True)