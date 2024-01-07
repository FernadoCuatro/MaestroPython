class Pelicula(object):

	# Constructor de clase
	def __init__(self, titulo, duracion, lanzamiento):
		self.titulo = titulo
		self.duracion = duracion
		self.lanzamiento = lanzamiento
		print("{} con duracion de {} minutos, se estrena {}, Vivela!".format(self.titulo, self.duracion, self.lanzamiento))

	# metodo destructor
	def __del__(self):
		print("Se acabo el estreno de",self.titulo)

	# str(10)
	# Redifinimos el metodo string
	def __str__(self):
		return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

	# redifiniendo el metodo lenght
	def __len__(self):
		return self.duracion


p = Pelicula("The grand tour", 73, "17 de diciembre")
print(str(p))
print(len(p))
# del(p)