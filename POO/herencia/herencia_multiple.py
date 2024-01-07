class A():

	def __init__(self):
		print("Soy de clase A")
	def a(self):
		print("Este metodo lo heredo de A")
		
class B():

	def __init__(self):
		print("Soy de clase B")
	def b(self):
		print("Este metodo lo heredo de B")

# A TODO SE LE PASA SELF

# Al momento de heredar, toma como
# prioridad la clase que se hereda
# que este mas a la izquierda
class C(B,A):
	def c(self):
		print("Este metodo es de C")

c = C()
c.a()
c.b()
c.c()