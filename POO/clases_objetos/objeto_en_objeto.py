class Pelicula:
	# Constructor de clase
	def __init__(self, titulo, duracion, lanzamiento):
		self.titulo = titulo
		self.duracion = duracion
		self.lanzamiento = lanzamiento
		print("{} con duracion de {} minutos, se estrena {}".format(self.titulo, self.duracion, self.lanzamiento))

	def __str__(self):
		return "{} ({})".format(self.titulo, self.lanzamiento)

class Catalogo():
	# lista vacia
	peliculas = []

	def __init__(self, peliculas=[]):
		self.peliculas = peliculas

	def agregar(self, p):
		self.peliculas.append(p)

	def mostrar(self):
		for p in self.peliculas:
			print(p)

# Creamos una pelicula
p = Pelicula("Batman Begins", 140,"2005")
# Creamos un catalogo
c = Catalogo([p])

# Mostramos todas las peliculas
# c.mostrar()

# Agregamos la pelicula de otra forma, por medio del metodo de catalogo
c.agregar(Pelicula("The Dark Knight", 152,"2008"))
c.agregar(Pelicula("The Dark Knight Rises", 165,"2010"))

print()
print("---------")
print()

c.mostrar()