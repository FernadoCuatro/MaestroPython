def mi_funcion(algo = None):
	try:
		if algo is None:
				# print("error, no se permite el valor nulo")
				raise ValueError("error, no se permite el valor nulo")
	except ValueError:
		print("error, no se permite el valor nulo (desde la except)")
	

# mi_funcion("algo")
mi_funcion()