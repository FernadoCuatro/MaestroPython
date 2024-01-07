# Los import necesarios
from tkinter import *

root = Tk()

# Aprendiendo a crear Menus
menubar = Menu(root)
root.config(menu = menubar)

# Creamos submenus 

# Agregar comandos a una opcion de un menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label = "Nuevo")
filemenu.add_separator()
filemenu.add_command(label = "Abrir")
filemenu.add_command(label = "Guardar")
filemenu.add_separator()
filemenu.add_command(label = "Cerrar archivo")
filemenu.add_separator()
filemenu.add_command(label = "Salir", command = root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Cortar")
editmenu.add_command(label = "Copiar")
editmenu.add_command(label = "Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label = "Mas información")

menubar.add_cascade(label = "Archivo", menu = filemenu)
menubar.add_cascade(label = "Editar", menu = editmenu)
menubar.add_cascade(label = "Ayuda", menu = helpmenu)



# Siempre abajo del todo
root.mainloop()