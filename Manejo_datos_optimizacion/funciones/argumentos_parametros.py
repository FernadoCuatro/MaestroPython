# Sumatoria de dos numeros por medio de parametros y argumentos
def suma(a,b):
	return a+b

# print(suma(2,423))

# argumentos por posición
def resta(a,b):
	return a-b;
# resta(1,2)
# resta(b=2,a=1)

# Asignar valores por defecto
def resta(a=None, b=None):
	if a == None or b == None:
		print("Error, debes enviar dos numeros a la funcion")
		return
	else:
		return a-b;

#resta()