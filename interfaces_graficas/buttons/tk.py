# Los import necesarios
from tkinter import *

# Creamos una funcion
def hola():
 print("Hola mundo")

def crear_label():
 Label(root, text = "Hola mundo").pack()

root = Tk()

# La funcion que mandamos a usar en el comportamiento debe de estar 
# Creada antes para que funcione

# Creamos un buttom
Button(root, text = "Iniciar", command = crear_label).pack()

# Siempre abajo del todo
root.mainloop()