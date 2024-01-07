# Los import necesarios
from tkinter import *
# Importamos los Popups
from tkinter import messagebox as MessageBox

root = Tk()

# Muestra un icono y un mensaje
# Tres variades para mostrar mensajes directos
# MessageBox => Aceptar, alerta, aceptar o rechazar
def test():
 #                   1. Titulo de la ventana | 2. Contenido del mensaje
 MessageBox.showinfo("Aviso","La informacion solicitada no es valida.")
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

Button(root, text="¿Que pasara?", command = test).pack()

# Siempre abajo del todo
root.mainloop()