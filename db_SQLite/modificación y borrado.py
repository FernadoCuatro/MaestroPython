import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

# Para hacer un select * from where
# se hace como siempre
# Y como es para sacar solo un dato se usa:
# usuario = cursor.fetchone()

# .fetchone() cada vez que se escribe baja a la siguiente posicion el cursor

# Para el update, es lo mismo tambien, la misma sintaxis

# El delete de igual forma, como siempre


conexion.commit()
conexion.close()