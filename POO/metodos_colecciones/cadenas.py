c = "100"
c2 = "ABC23c"
# La cadena es numero?
print(c.isdigit()) 

# La cadena contiene los numeros alfanumericos? Sin caracteres especiales
print(c2.isalnum())

# Tenemos unicamente letras?
# El espacio ' ' no cuenta como caracter del alfabeto
print(c2.isalpha())

# Todo los caracteres son minusculas o mayusculas?
print(c2.islower())
print(c2.isupper())

# EL texto es un titulo?
print(c2.istitle())

# La cadena lleva espacio, es toda de espacio?
print(c2.isspace())

# La cadena empieza con una letra es especifico?
# Tambien se puede con cadena, solo letra o solo cadena
print(c2.startswith('A'))

# Para comprobar si acaba de una forma
print(c2.endswith('C'))

print()
print("------------------------")

# Cadena en mayusculas
print("holamundo".upper())
# Minusculas 
print("holamundo".lower())
# Poner la primera letra de la frase en mayuculas
print("holamundo".capitalize())
# Todas las palabras con la primera en mayuscula
print("hola mundo".title())

print()
print("------------------------")

# Contar cuantas veses aparece la O 
print("hola mundo".count('o'))
# Cuantas veces aparece Mundo
print("hola mundo".count('mundo'))

# Buscar en que lugar aparece dentro del indice
# Empienza en el indice 5
print("hola mundo".find('mundo'))

# Encotrar la ultima aparicion
# revert find (Busqueda al reves)
print("hola mundo hola mundo".rfind('mundo'))

print()
print("------------------------")

# Metodos especiales

# Split()[0] separa las palabras que devuelve una lista, tipo array

# Separar sabiendo que una coma separe las palabras, las separa a traves del caracter
# Split(',')[0]

# Join nos separa cada caracter con el que le mandemos como parametro
# ",".join("Hola mundo")
# Retorna: "H,o,l,a ,m,u,n,d,o"

# Tenemos una cadena con varios espacios adelante o detras y luego el texto
# Con el metodo strip() borramos los espacios
# si mandamos el paramtros es lo que elimina strip('-')

# Remplace, cambia una letra o una cadena de una cadena 
# Le decimos que cambie la o por el 0
print("Hola mundo".replace('o','0'))
print("Hola mundo".replace('mundo','melissa'))

# Le decimemos que borre la palabra mundo solamente 3 veces
print("Hola mundo mundo mundo mundo".replace(' mundo','',3))