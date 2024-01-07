# Los import necesarios
from tkinter import *

# Creamos la raiz
# la T en Mayus
root = Tk()

# Titulo de la ventana
root.title("Welcome")
# Redimencionable
# Los 0 vendrian hacer un true o false
# root.resizable(0,0)

# El icono de arriba
# Debe ser .ico
root.iconbitmap("hola.ico")

# truco
# Renombrar el nombre del archivo
# Para forzar un ejecutable de windows
# tk.py => tk.pyw


# Siempre abajo del todo
root.mainloop()