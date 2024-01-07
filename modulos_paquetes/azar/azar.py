# importamos
import random

# Generar un flotante al azar
print(random.random()) # Mayor que 0 pero menor que 1

# rango flotante al buscar ese numero
print(random.uniform(1,10)) # Mayor que uno pero menor que diez

# Generar enteros
print(random.randrange(10)) # Menor que diez

# Al azar multiplo de dos
print(random.randrange(0,101,2))

# Escojer una letra de una cadena 
c = "hola mundo"
print(random.choice(c))

# Eso tambien sirve con las listas

# Metodo que bajaraja de colecciones
# random.shuffle()

# Tomar una muestra aleatoria
# random.sample(l, 2)