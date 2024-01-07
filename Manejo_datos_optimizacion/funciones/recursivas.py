# La recursividad es hacer un problema en problemitas mas pequeños
# Es como un espejo enfrente de otro espejo
# Cuando una funcion se manda a llamar a si misma
def cuenta_atras(num):
	num -= 1
	if num > 0:
		print(num)
		cuenta_atras(num)
	else:
		print("\nFIN!\n")
	print("Fin de la funcion", num)

# cuenta_atras(5)

# factorial de un numero
def factorial(num):
	# print("Valor inicial =>", num)
	if num > 1:
		num = num * factorial(num-1)
	# print("Valor final =>",num)
	return num

print(factorial(5))