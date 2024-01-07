# Los import necesarios
from tkinter import *
# Importamos los Popups
from tkinter import messagebox as MessageBox
# Importar para seleccionar color
from tkinter import colorchooser as ColorChooser
# Importar para seleccionar archivos
from tkinter import filedialog as FileDialog

root = Tk()

# Muestra un icono y un mensaje
# Tres variades para mostrar mensajes directos
# MessageBox => Aceptar, alerta, aceptar o rechazar
def test():
 #                   1. Titulo de la ventana | 2. Contenido del mensaje
 # MessageBox.showinfo("Aviso","La informacion solicitada no es valida.")
 # MessageBox.showwarning("Cuidado","Si no te dice nada, es porque es un no.")
 # MessageBox.showerror("Error","No se pudo, a pesar del intento.")

 # Tipo pregunta si or no
 # resultado = MessageBox.askquestion("Salir", "¿Esta seguro que desea salir?")
 # Devuelve: Yes / No
 #if resultado == "yes":
 # root.destroy()

 # Tipo aceptar o cancelar
 # resultado = MessageBox.askokcancel("¿Seguro?", "¿Remplazar el fichero actual?")
 # if resultado:
 #  root.destroy()

 # Tipo aceptar(si) o cancelar(no)
 # resultado = MessageBox.askyesno("¿Seguro?", "¿Remplazar el fichero actual?")
 # if resultado:
 #  root.destroy()

 # Intentar | true o false
 # MessageBox.askretrycancel("¿Seguro?", "¿Reintentar?")

 # Elegir un color
 # color = ColorChooser.askcolor(title="Selecciona un color")
 # print(color)

 # Conseguir la ruta de los ficheros
 # initialdir ="C:" <= Donde inicia la busqueda de raiz de archivos
 # filetypes  = Busqueda de archivos 
 # ruta = FileDialog.askopenfilename(title="Abrir un fichero", 
 #  filetypes = (
 #   ("Ficheros de texto","*.txt"),
 #   ("Imagenes","*.jpg"),
 #   ("Todos los ficheros","*.*")
 #   ))
 # print(ruta)

 # Donde guardar, guardar datos en un directorio
 # Abre un fichero en w, es decir que lo reeemplaza, es decir borra todo y deja todo y lo remplaza
 # Duvuelve un fichero con este modelo:
 # <_io.TextIOWrapper name='C:/Users/Fernando/Desktop/hola.txt' mode='w' encoding='cp1252'>
 fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode = "w", defaultextension=".txt")
 if fichero is not None:
  fichero.write("Hola mundo")
  fichero.close()





Button(root, text="¿Que pasara?", command = test).pack()

# Siempre abajo del todo
root.mainloop()