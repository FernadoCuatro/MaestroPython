try:
	n = float(input("introduce un numero: "))
	5/n
except TypeError:
	print("No se puede dividir el numero por una cadena")
except ValueError:
	print("Debes introducir una cadena que sea un numero")
except ZeroDivisionError:
	print("La division no se puede efectuar")
except Exception as e:
	print(type(e).__name__)

input()