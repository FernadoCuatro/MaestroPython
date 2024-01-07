# Buscamos el path del archivo
import sys

sys.path.insert(1, '..')
#print(sys.path)

# import saludos
# saludos.saludar()

# Esto importa solamente una funcion 
# from saludos import saludar

# Esto importa todas las funciones o clases
from saludos import *

saludar()
saludo()
