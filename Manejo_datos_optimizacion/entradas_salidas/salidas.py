v = "otro texto"
n = 10
print("Un texto", v, "y un número", n)

print()
# Formateo de escritura
c = "Un texto {} y un número {}".format(v, n)
print(c)

print()
# de forma ordenada
print("Un texto {1} y un número {0}".format(v, n))

print()
# Con un codigo
print("Un texto {texto} y un número {numero}".format(texto=v, numero=n))

# Aliniar palabras
print("{:>30}".format("Palabra"))
print("{:30}".format("Palabra"))
print("{:^30}".format("Palabra"))

# Truncar 
print("{:.3}".format("Palabra"))

# Truncar y aliniar 
print("{:>30.3}".format("Palabra"))

# Redonder numeros decimales y formateo de numeros enteros con espacio
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

print()
# Redonder numeros decimales y formateo de numeros enteros con ceros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

print()
# Formateo de numero flotantes rellenandno los espacios
print("{:7.3f}".format(3.14159226))
print("{:7.3f}".format(153.21))

print()
# Formateo de numero flotantes rellenandno los espacios con ceros
print("{:07.3f}".format(3.14159226))
print("{:07.3f}".format(153.21))
