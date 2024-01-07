# Encapsulacion: Funcionalidad para impedir acceso a clases o metodos
# PYTHON NO LO TIENE

class ejemplo:
	# atributo privado
	# Siempre va precedido por __
	__atributo_privado = "Soy un atributo inalcanzable desde afuera"

	def __metodo_privado(self):
		print("Soy un inalcanzable desde afuera")

	def atributo_publico(self):
		return self.__atributo_privado

e = ejemplo()

# Da error
# e.__atributo_privado

# Da error
# e.__metodo_privado

print(e.atributo_publico())