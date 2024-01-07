# Un parametro que se aumente *args
def indeterminados_posicion(*args):
	print(args)

# Para recorrer cada uno de los elementos 
#	for arg in args:
#		print(arg)

# indeterminados_posicion(1,"Hola", [1,2,3,4])
# Tenemos una tupla de regreso, ya que no podemos modificarla. 

# Cuando pasamos los parametros por nombre, python nos arma un diccionario. 
def indeterminados_nombre(**kwargs):
#	print(kwargs)
# Para recorrerlos
	for kwarg in kwargs:
		print(kwarg, "=>", kwargs[kwarg])

# indeterminados_nombre(c=1,n="Hola", l=[1,2,3,4])

# Una funcion con un poco de todo
def super_funcion(*args,**kwargs):
	total = 0
	for arg in args:
		total += arg
	print("Sumatorio indeterminado es:", total)

	for kwarg in kwargs:
		print(kwarg, "=>", kwargs[kwarg])

super_funcion(10,50,-1,1.56,13.5,nombre="Hector",edad=27)