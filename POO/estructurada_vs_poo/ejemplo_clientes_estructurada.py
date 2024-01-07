# Ejemplo de implementacion con programacion estrucurada

# Lista clientes
clientes = [
	{'Nombre': 'Hector', 'Apellidos': 'Costa Guzman',     'dni': '11111111A'},
	{'Nombre': 'Juan',   'Apellidos': 'Gonzales Marquez', 'dni': '22222222B'}
]

# Accedemos a la lista clientes
# print(clientes)

# funcion
# Mostrar atraves del ID
def mostrar_cliente(clientes, dni):
	for c in clientes:
		if (dni == c['dni']):
			print('{} {}'.format(c['Nombre'], c['Apellidos']))
			return
	print('Cliente no encontrado')

# Accedemos a la funcion definida arriba 
# le pasamos la lista de clientes y el DNI a buscar 
mostrar_cliente(clientes, '11111111A')

print()
print("--------------------")
print()

# funcion
# borrar un clientr a traves de un ID
def borrar_cliente(clientes, dni):
	for i, c in enumerate(clientes):
		if (dni == c['dni']):
			del(clientes[i])
			print(str(c), "> Borrado")
			return
	print('Cliente no encontrado para borrar')

borrar_cliente(clientes, '11111111A')

print()
print("--------------------")
print()

print(clientes)
# Esto para que no se cierre la consola
input()