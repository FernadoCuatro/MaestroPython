# Los import necesarios
from tkinter import *

# Configuracion de la raiz
root = Tk()

# frame = Frame(root)
# frame.pack()
# # Creamos una entrada 
# entry = Entry(frame)
# entry.pack(side = "right")
# # Creamos la label
# label = Label(frame, text = "Nombre: ")
# label.pack(side = "left")

# frame_2 = Frame(root)
# frame_2.pack()
# # Creamos una entrada 
# entry_2 = Entry(frame_2)
# entry_2.pack(side = "right")
# # Creamos la label
# label_2 = Label(frame_2, text = "Apellido: ")
# label_2.pack(side = "left")

# Creamos la label
label = Label(root, text = "Nombre completo: ")
label.grid(row = 0, column = 0, sticky="e", padx = 0, pady = 5)
# Creamos una entrada 
entry = Entry(root)
entry.grid(row = 0, column = 1, padx = 5, pady = 5)
entry.config(justify = "right", state = "disabled")

# Creamos la label
label_2 = Label(root, text = "Contraseña: ")
label_2.grid(row = 1, column = 0, sticky="e", padx = 0, pady = 5)
# Creamos una entrada 
entry_2 = Entry(root)
entry_2.grid(row = 1, column = 1, padx = 5, pady = 5)
entry_2.config(justify = "center", show = "-")

# pack nos posiciona los elementos en una linea
# De esta forma se posiciona mal dentro de la raiz 
#                    _____________   _____________
# Nombre: Apellido: |_____________| |_____________| 

# Para colocar bien, haremos dos frame 


# Siempre abajo del todo
root.mainloop()