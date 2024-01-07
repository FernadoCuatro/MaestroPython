# La pila solo permite agregar o eliminar elementos
# El ultimo elemento en entrar es el primero en salir 

# Se simula la lista en python ya que aqui no existen

pila = [3,4,5]

# Agregamos
pila.append(6)
pila.append(7)

print(pila)

# Sacamos elementos
pila.pop()

print(pila)

# Guardamos la variable en salida 
n = pila.pop();
print(n)

# Las colas
# En las colas el primero en entrar es el primero en salir
# Las librerias se llaman modulos

from collections import deque

# Cola vacia
cola = deque()
print(cola)

cola = deque(['Hector', 'Juan', 'Miguel'])
print(cola)

cola.append('Maria')
cola.append('Nicolo')
print(cola)

# Sacar los datos de la cola
cola.popleft()
print(cola)

p = cola.popleft()
print(cola)