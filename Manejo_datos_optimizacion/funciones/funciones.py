# Para declara una funcion usamos 'def'
def saludar():
	print("Este print se llama desde la funcion saludar()")

# saludar()

# Pra definir los nomnbres de funciones es recomendable usar minusculas 
# Y palabras separadas con _ en caso de colocar espacios
# Y utilizar nombres auto explicativos

# funcion que dibuje la tabla de numero 5
def dibujar_tabla_5():
	for i in range(1,11):
		print("5 * {} = {}".format(i, i*5))

# dibujar_tabla_5()

# Tenemos que tener en cuenta el ambito de las variables 
# Lo de siempre del Scope de las variables

# Retornando valores de una variable
def retorne_string():
	return "Una cadena retornada"

# retorne_string()
# print(retorne_string())
# c = retorne_string()
# print(c)

# retornar diferentes valores
def retornar_valores():
	return "Una cadena", 20, [1,2,3]
