# Importamos pickle
import pickle

lista = [1, 2, 3, 4, 5]

# Guardamos en fichero Y lo abrimos
# wb / write binary / Escritura binaria
fichero = open("lista.pckl", "wb")

# Borra el contenido del fichero, y escribe lo nuevo
pickle.dump(lista, fichero)

fichero.close()

# Recuperamos la informacion en el archivo con pickle
# rb / read binary / lectura binaria
fichero = open("lista.pckl", "rb")

lista_nueva = pickle.load(fichero)
# print(lista_nueva)


# -----------------------------------------

# Creamos una clase y un objeto en un archivo
class Persona:

	def __init__(self, nombre):
		self.nombre = nombre

	def __str__(self):
		return self.nombre

nombres = ["Hector", "Mario", "Marta", "Melissa"]
personas = []

for n in nombres:
	p = Persona(n)
	personas.append(p)

# Guardar en un fichero las personas
fichero_p = open("persona.pckl", "wb")
pickle.dump(personas, fichero_p)
fichero_p.close()

# Recuperamos la infomacion
fichero_p = open("persona.pckl", "rb")
personas_n = pickle.load(fichero_p)
fichero_p.close()

for p in personas_n:
	print(p)