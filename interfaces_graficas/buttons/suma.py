# Los import necesarios
from tkinter import *

def sumar():
 rs.set(int(n1.get()) + int(n2.get()))
 borrar()

def resta():
 rs.set(int(n1.get()) - int(n2.get()))
 borrar()

def multiplicar():
 rs.set(float(n1.get()) * float(n2.get()))
 borrar()

def borrar():
 n2.set('')
 n1.set('')

root = Tk()
root.config(bd = 15)

n1 = StringVar()
n2 = StringVar()
rs = StringVar()

entry_1 = Entry(root, justify = "center", textvariable = n1) # Primer numero
entry_1.grid(row = 0, column = 1)

label_1 = Label(root, text = "")
label_1.grid(row = 0, column = 2)

entry_2 =Entry(root, justify = "center", textvariable = n2) # Segundo numero
entry_2.grid(row = 0, column = 3)

label_2 = Label(root, text = "=")
label_2.grid(row = 0, column = 4)

entry_3 =Entry(root, justify = "center", textvariable = rs, state = "disabled") # Resultado
entry_3.grid(row = 0, column = 5)

Button(root, text = "+", command = sumar).grid(row = 1, column = 1, padx = 0, pady = 10)
Button(root, text = "-", command = resta).grid(row = 1, column = 3, padx = 0, pady = 10)
Button(root, text = "*", command = multiplicar).grid(row = 1, column = 5, padx = 0, pady = 10)


# Siempre abajo del todo
root.mainloop()