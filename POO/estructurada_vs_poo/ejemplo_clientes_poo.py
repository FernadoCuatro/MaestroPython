""" Ejemplo de implementación con Programación Orientada a Objetos
No hace falta entender el código, lo aprenderemos en esta unidad """

class clientes:
 """docstring for clientes"""
 def __init__(self, dni, nombre, apellidos):
  super(clientes, self).__init__()
  self.dni = dni
  self.nombre = nombre
  self.apellidos = apellidos

 def __str__(self):
 	return '{} {}'.format(self.nombre,self.apellidos)

class Empresa:
	"""docstring for Empresa"""
	def __init__(self, clientes=[]):
		super(Empresa, self).__init__()
		self.clientes = clientes

	def mostrar_cliente(self, dni=None):
		for c in self.clientes:
			if c.dni == dni:
				print(c)
				return
		print("Cliente no encontrado")
		
	def borrar_cliente(self, dni=None):
		for i,c in enumerate(self.clientes):
			if c.dni == dni:
				del(self.clientes[i])
				print(str(c),"> BORRADO")
				return
		print("Cliente no encontrado")

# Agregamos nuevos clientes
hector = clientes(dni="1111111A", nombre="Hector", apellidos="Costa Guzman")
juan = clientes("2222222B", "Juan", "Gonzlaes Marquez")

# Agregamos una empresa
# Con los clientes que ya tenemos
empresa = Empresa(clientes=[hector, juan])

print(empresa.mostrar_cliente('1111111A'))

# Esto para que no se cierre la consola
input()