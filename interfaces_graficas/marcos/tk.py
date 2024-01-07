# Los import necesarios
from tkinter import *

# Creamos la raiz
root = Tk()

# Titulo de la ventana
root.title("Inicio")
root.resizable(0,0)
root.iconbitmap("hola.ico")

# Creamos un frame
frame = Frame(root, width = 400, height = 400)

# Lot empaquete y lo destribuya
frame.pack()

# Definir el tamaño del frame
# frame.config(width = 400, height = 400)
#frame.config(cursor="pirate")
# Cambiar el fondo
frame.config(bg="#eee")
#borde
frame.config(bd=25)
# frame.config(relief="sunken")

# Tambien lo podemos usar con root, las mismas configuraciones

# Distrubucion del widget
# Siempre lo pondra arriba al centro

# Lado a distribuir el marco a la derecha
# frame.pack(side="right") #bottom #left # top
# Anclado a una posicion 
# frame.pack(side="right", anchor="e") e => este (Punto cardinales e ingles)

# Rellenar del contenedor padre
# frame.pack(fill="x") x => de los lados y => a lo alto

# frame.pack(fill="both", expand = 1) => Se expande con un 1 como un true, both tambien se manda para rellenar 


# Siempre abajo del todo
root.mainloop()