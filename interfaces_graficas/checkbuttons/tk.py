# Los import necesarios
from tkinter import *

def seleccionar():
 cadena = ""

 if leche.get():
  cadena += "Su cafe llevara leche"
 else:
  cadena += "Su cafe sera sin leche"

 if azucar.get():
  cadena += " y con azucar"
 else:
  cadena += " y sin azucar"

 monitor.config(text = cadena)

# Configuracion de la raiz
root = Tk()
root.title("Cafeteria")
root.config(bd = 15)

# Checkbuttons
leche = IntVar() # 1 => si | 0 => no
azucar = IntVar() # 1 => si | 0 => no

imagen = PhotoImage(file = "imagen.gif")
Label(root, image = imagen).pack(side = "left")

frame = Frame(root)
frame.pack(side = "left")

Label(frame, text = "¿Como quieres el cafe?").pack(anchor = "w", padx = 0, pady = 10)
Checkbutton(frame, text = "Con leche", variable = leche, onvalue = 1, offvalue = 0, command = seleccionar).pack(anchor = "w")
Checkbutton(frame, text = "Con Azucar", variable = azucar,  onvalue = 1, offvalue = 0, command = seleccionar).pack(anchor = "w")

monitor = Label(frame)
monitor.pack()

# Siempre abajo del todo
root.mainloop()