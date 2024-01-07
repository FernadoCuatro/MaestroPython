# Son colecciones desordendas de elementos unicos

# Conjunto vacio
conjunto = set()

# Conjunto con varios elementos
conjunto = {1,2,3}

print(conjunto)

# Add el mas utilizado
conjunto.add(4)
print(conjunto)

conjunto.add(0)
print(conjunto)

conjunto.add("H")
print(conjunto)

conjunto.add("A")
print(conjunto)

conjunto.add("Z")
print(conjunto)

# Grupo de personas
grupo = {"Hector", "Juan", "Marios"}

print("Hector" in grupo)
print("Maria" in grupo)
print("Hector" not in grupo)

# No pueden existir dos elementos iguales 

test = {"Hector", "Hector", "Hector"}
print(test)

# Lista a conjunto
l = [1,2,3,3,2,1]

# Hacemos un cast
# De lista a conjunto 
c = set(l)

print(c)

# De conjutno a lista
l = list(c)
print(l)

l = [1,2,3,3,2,1]
print(l)

l = list(set(l))
print(l)

# En cadena
s = "Al pan pan y al vino vino"
print(s)

# Haciendo un conjunto
print(set(s))
