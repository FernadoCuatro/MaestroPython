# producto (Superclase)
# adorno | Alimento | libro (Subclases) 

class Producto:
	def __init__(self, referencia, nombre, pvp, descripcion):
		self.referencia  = referencia
		self.nombre      = nombre
		self.pvp         = pvp
		self.descripcion = descripcion
		print("Referencia: {}\tNombre: {}\tPVP: {}\tDescripcion:{}".format(self.referencia, self.nombre, self.pvp, self.descripcion))


# Subclase, le pasamos copia de la clase que hereda
class Adorno(Producto):
	pass

# a = Adorno(2034, "Vaso adornado", 15, "Vaslo de porcelana adornado con arboles")

class Alimento(Producto):
	productor = ""
	distribuidor = ""

	print("Productor: {}\tDistribuidor: {}\t".format(productor, distribuidor))

a = Alimento(2034, "Vaso adornado", 15, "Vaslo de porcelana adornado con arboles")
a.productor = "La aceitera"
a.distribuidor = "Distrubuciones SA"
		
class Libro(Producto):
	isbn = ""
	autor = ""
	print("isbn: {}\autor: {}\t".format(isbn, autor))

	
# Asi se haria normalmente
# class Producto:
# 	"""docstring for Producto"""
# 	def __init__(self, referencia, tipo, nombre, pvp, descripcion, productor = None, distribuidor = None, isbn = None, autor = None):
# 		self.referencia = referencia
# 		self.tipo = tipo
# 		self.nombre = nombre
# 		self.pvp = pvp
# 		self.descripcion = descripcion
# 		self.productor = productor
# 		self.distribuidor = distribuidor
# 		self.isbn = isbn
# 		self.autor = autor

# adorno = Producto("000A", "ADORNO", "Vaso adornado", 15, "Vaso de porcelana condibujos")
# print(adorno.tipo)