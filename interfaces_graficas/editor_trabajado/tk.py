# Los import necesarios
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from io import open

# La usaremos para almacenar la ruta de un fichero
ruta = ""

def nuevo():
 global ruta
 mensaje.set("Nuevo fichero")
 ruta = ""
 # Que borreo desde el caracter 1 hasta el ultimo
 # Dentro de un text el primer caracter siempre es un \n (salto de linea)
 texto.delete(1.0, "end")
 root.title("Editor de texto - F4")

def abrir():
 global ruta
 mensaje.set("Abrir fichero ¿Cual?")

 ruta = FileDialog.askopenfilename(initialdir = ".", filetype = (("Ficheros de texto", "*.txt"),), title = "Abrir un fichoro de texto")
 if ruta != "":
  fichero = open(ruta, "r")
  contenido = fichero.read()
  texto.delete(1.0, "end")
  texto.insert("insert", contenido)
  fichero.close()
  root.title(ruta + " -  F4")

def guardar():
 global ruta
 mensaje.set("Guardar fichero ¿Donde?")

 if ruta != "":
  contenido = texto.get(1.0, "end-1c")
  fichero = open(ruta, "w+")
  fichero.write(contenido)
  fichero.close

  mensaje.set("¡Se guardo el fichero correctamente!")
 else:
  guardar_como()

def guardar_como():
 global ruta
 mensaje.set("Vamo a guardar")
 fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode = "w", defaultextension = ".txt")
 if fichero is not None:
  ruta = fichero.name
  contenido = texto.get(1.0, "end-1c")
  fichero = open(ruta, "w+")
  fichero.write(contenido)
  fichero.close
  root.title(ruta + " -  F4")
 else: 
  mensaje.set("cancelaste al guardar, no pasa nada.")
  ruta = ""

def salir():
 resultado = MessageBox.askquestion("Salir", "¿Esta seguro que desea salir?")
 if resultado == "yes":
  root.destroy()

root = Tk()
root.title("Editor de texto - F4")

# Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Nuevo", command = nuevo)
filemenu.add_command(label = "Abir", command = abrir)
filemenu.add_command(label = "Guardar", command = guardar)
filemenu.add_command(label = "Guardar como", command = guardar_como)

menubar.add_cascade(menu = filemenu, label = "Archivo")
menubar.add_cascade(label = "Cerrar el editor", command = salir)
root.config(menu = menubar)

# Caja de texto central
texto = Text(root)
texto.pack(fill =  "both", expand = 1)
texto.config(bd = 0, padx = 6, pady = 4,  font = ("Victor Mono Medium", 15))

# Monitor inferior para el usuario
mensaje = StringVar()
mensaje.set("¡Bienvenido a tu editor! ¿Que haremos hoy?")
monitor = Label(root, textvar = mensaje, justify="left")
monitor.pack(side = "left")

# Siempre abajo del todo
root.mainloop()