# Para manejar las expeciones, con lo de siempre try el codigo propenso.
while (True):
	try:
		n = float(input("Introduce un numero: "))
		m = 4

		print("{} / {} = {}".format(n, m, n/m))
		# break # Con esto cortamos el while para que no siga pidiendo los datos
	except:
		print("Ha ocurrido un error.")
	else:
		print("Todo a funcionado correctamente")
		break # Con esto cortamos el while para que no siga pidiendo los datos
	finally:
		print("Fin del sistema")


# Siempre cuando se habra de consola, usar esto. 
input()