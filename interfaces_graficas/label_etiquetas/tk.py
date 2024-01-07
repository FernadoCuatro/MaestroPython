# Los import necesarios
from tkinter import *

# Creamos la raiz
root = Tk()

# Para hacer el texto dinamico debe colocarse la string var
# abajo de la raiz

# Variables dinamicas
texto = StringVar()
texto.set("La imagen con la tazita")

imagen = PhotoImage(file = "imagen.gif")
Label(root, image =  imagen, bd = 0).pack()

# Titulo de la ventana
root.title("Inicio")
root.resizable(0,0)
root.iconbitmap("hola.ico")

# Creamos un frame
frame = Frame(root, width = 480, height = 320)

# Lot empaquete y lo destribuya
frame.pack()

# Widget para los label
#Label(frame, text = "Label 1 [50x50]").place(x = 50, y = 50)
# Siempre hay que empaquetar
# Pero no con pack porque el tamaño lo reinicia
# Lo hacemos con place 
# Cordenada x / y para establecer el lugar

# Con el pack pine un alinea cada widget y lo deja al centro
# Label(frame, text = "Label 2 [100x100]").place(x = 100, y = 100)
# Label(frame, text = "Label 3 [150x150]").place(x = 150, y = 150)
# Label(frame, text = "Label 4 [200x200]").place(x = 200, y = 200)
# Label(frame, text = "Label 5 [250x250]").place(x = 250, y = 250)

# Label con mas configuraciones
config_1 = Label(frame, text = "Configuracion nueva")
config_1.pack(side = "left")
config_1.config(bg = "green", fg = "white", font = ("Verdana", 24))

# Hacer el texto dinamico 
config_1.config(textvariable = texto)

# Las etiquetas pueden tener imagenes
# Tkinter solo soporta dos formatos de imagenes
# pgm y gif

# Siempre abajo del todo
root.mainloop()