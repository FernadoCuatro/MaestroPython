# Cuando se envian por valor, se envia una copia del valor que enviamos
# En sus propias variables

def doblar_valor(numero):
	numero*=2

n = 10
doblar_valor(n)
print(n)

# Cuando se pasa por referencia, se manejan los datos originales
def doblar_valores(numeros):
	for i,n in enumerate(numeros):
		numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns)
print(ns)


# Se puede asignar y deducir cuando algo se pasa por valor, y cuando algo se pasa por referencia.

# Cuando pasamos por valor, pordemos reasignar el valor que nos devuelve la funcion con return a la variable nueva
# Y cuando pasamos por referencia, pordemos mandar una copia de lo que estamos manejando, en el caso de las litas con el [:]