# Importamos lo necesario
from io import open
import pickle

# Construimos la clase
class Pelicula:

 def __init__(self, titulo, duracion, lanzamiento):
  self.titulo = titulo
  self.duracion = duracion
  self.lanzamiento = lanzamiento
  print("Se agrego la pelicula:", self.titulo)

  def __str__(self):
   return "{} => ({})".format(self.titulo, self.lanzamiento)


class Catalogo:
 peliculas = []

 # Constructor de la clase
 def __init__(self):
  # Cargar el fichero en el fichero
  self.cargar()

 def agregar(self, p):
  self.peliculas.append(p)
  self.guardar()

 def mostrar(self):
 	if len(self.peliculas) == 0:
 		print("Catalogo vacio")
 	else:
 		for p in self.peliculas:
 			print(str(p))

 def cargar(self):
 	# apeend binary + read
 	fichero = open("catalogo.pckl", "ab+")
 	# Como es un append se ira el puntero al final
 	# Hacemos un seek para traerlo al principio
 	fichero.seek(0)

 	try:
 		# Leermos las peliculas
 		self.peliculas = pickle.load(fichero)
 	except:
 		print("El fichero esta vacio")
 	finally:
 		fichero.close()
 		print("Total de peliculas => {}".format(len(self.peliculas)))

 def guardar(self):
 	fichero = open("catalogo.pckl", "wb")
 	pickle.dump(self.peliculas, fichero)
 	fichero.close()

 # Destructor de la clase
 def __del__(self):
 	self.guardar()
 	print("Se ha guardado el fichero")

# Creamos un catalogo
c = Catalogo()

# Mostramos el catalogo
# c.mostrar()

# Creamos una pelicula
c.agregar(Pelicula("Batman Begins", 140, "15 de junio de 2005"))
c.agregar(Pelicula("The Dark Knight", 152, "18 de julio de 2008"))
c.agregar(Pelicula("The Dark Knight Rises", 165, "20 de julio de 2012"))

# Mostramos el catalogo
c.mostrar()

del(c)

input()