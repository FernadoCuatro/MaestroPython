# Son inmutables y los datos no se pueden modificar 

tupla =  (100, "Hola", [1,2,3,4,5], -50)
print(tupla)

# Tambien podemos accesdes desde los indices 
print(tupla[0])
print(tupla[-1])

# Tambien podemos usar el slicing
print(tupla[1:])

# Tambien podemos accedes a las listas
print(tupla[2][-1])

# Longitud 
print(len(tupla))

# .index para saber su posicion
print(tupla.index(100))
print(tupla.index("Hola"))

# Contar los elementos repetidos o no en una tupla
print(tupla.count(100))
print(tupla.count(9))

# El metodo append no funcioan en la tupla ya que la lista no se puede modificar
