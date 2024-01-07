# Son como lenjuages arreglos asociativo
# Llevan claves y el valor

# Diccionario vacio
vacio = {}
print(vacio)
print(type(vacio))

print()

# Diccionario de traducciones
colores = {
	'amarillo' : 'yellow',
	'azul' : 'blue',
	'verde' : 'green'
}
print(colores)

print(colores['azul'])

# Modificar un diccionario
colores['azul'] = 'white'
print(colores)

# Eliminar un dato del diccionario
del(colores['azul'])
print(colores)

# Tambien se puede manipular los datos dentro de un diccionario
# edades['Hector'] += 1
# edades['Juan'] + edades['maria']

print()
# Recorres un diccionario
for color in colores:
	print(color)

print()
# Solo la clave
for clave in colores:
	print(colores[clave])

print()
# O los dos
for clave in colores:
	print(clave, colores[clave])

print()
# La mehor forma de hacerlo
for c,v in colores.items():
	print(c, v)

print()
# Utilizarlo en conjunto con las listas

# Lista de personajes
personajes = []

# Creamos un diccionario
p = {
"Nombre":"Jack", 
"Numero":7, 
"Equipo":"Aston Villa"
}

# Lo añadimos a la lista
personajes.append(p)
print(personajes)

p = {
"Nombre":"Trippier", 
"Numero":21, 
"Equipo":"Atletico de Madrid"
}

# Lo añadimos a la lista
personajes.append(p)
print(personajes)

p = {
"Nombre":"Sterling", 
"Numero":7, 
"Equipo":"Manchester City"
}

# Lo añadimos a la lista
personajes.append(p)
print(personajes)

print()

for p in personajes:
	print(p['Nombre'], p['Numero'], p['Equipo'])