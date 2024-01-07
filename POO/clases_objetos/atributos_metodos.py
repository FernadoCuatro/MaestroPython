# Definimos una clase
# La clase es como un molde para crear objetos
class Galleta:
	pass

# La clase va en C para distinguir la sintaxis
# Estamos instanciando un objeto a partir de la clase
# Un objeto se crea a partir de una clase
una_galleta = Galleta()
otra_galleta = Galleta()

# Para saber el tipo de objeto
# print(type(una_galleta))

# Agregamos personalizacion a un metodo
una_galleta.sabor = "Salado"
una_galleta.color = "Marron"

# print("El sabor de esta galleta es",una_galleta.sabor)

# Personalizar los tributos
class Galleta:
	chocolate = False

# g = Galleta()
# g.chocolate = True
# print(g.chocolate)

# init y self
# Los metodos especiales se escriben con __ here __
# self, es como un this, hace referencia al propio metodo
# el self es un requisito
class Galleta():
	chocolate = False

	def __init__(self):
		print("Se acaba de crear una galleta")

	def chocolatear(self):
		self.chocolate = True

	def tiene_chocolate(self):
		if(self.chocolate):
			print("Soy una galleta chocolatada c:")
		else:
			print("Soy una galleta sin chocolate :c")

# g = Galleta()
# g.chocolatear()
# print(g.chocolate)
# g.tiene_chocolate()

# print()

# gl = Galleta()
# gl.tiene_chocolate()

class Galleta():
	chocolate = False

	# Si no se escriben los parametros, le pasamos los datos
	# por defecto de esta forma al hacer el objeto de la clase
	# No seran requeridos los argumentos 
	def __init__(self, sabor = None, color = None):
		# Hacemos referencia dentro del init
		self.sabor = sabor
		self.color = color

		if sabor is not None and color is not None:
			print("Se acaba de crear una galleta, con sabor {} y color {}".format(sabor, color))
		else:
			print("Se creo la galleta, sin mas")

	def chocolatear(self):
		self.chocolate = True

	def tiene_chocolate(self):
		if(self.chocolate):
			print("Soy una galleta chocolatada c:")
		else:
			print("Soy una galleta sin chocolate :c")

g = Galleta("Salada", "marron")
g = Galleta()

# Para que no se cierre
input()