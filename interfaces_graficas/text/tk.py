# Los import necesarios
from tkinter import *

root = Tk()

texto = Text(root)
texto.pack()
texto.config(width = 30, height = 10, font = 'arial', padx = 5, pady = 10, selectbackground = "blue")



# El 30 dentro del width es el numero de caracteres que se pueden escribir
# El 10 dentro del height son 10 caracteres para abajo

# Siempre abajo del todo
root.mainloop()