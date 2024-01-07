import sqlite3

# Conexion a base de datos
# Si no existe la base de datos
# Se crea automaticamente
# Se guarda .db por la extension del archivo
conexion = sqlite3.connect("ejemplo.db")

# Estrucutura principal para la base de datos
# Con el cursor ya podemos escribir escribir script en SQL
cursor = conexion.cursor()

# Sintaxis SQL, una consulta
# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INT, email VARCHAR(100))")

# Insertamos un registro
# cursor.execute("INSERT INTO usuarios VALUES ('Fernando', 21,'fernando@cuatro.com')")
# Tenemos que confirmar los cambios, para ejecutarlos

# cursor.execute("SELECT * FROM usuarios")
# Solo para un registro
# usuarios = cursor.fetchone()
# print(usuarios) # usuarios[0]

# Insertar varios registros a la vez
# usuarios = [
#  ('Mario', 51, 'mario@correo.com'),
#  ('Mercedes', 38, 'mercedes@correo.com'),
#  ('Juan', 19, 'juan@correo.com')
# ]

# cursor.executemany("INSERT INTO usuarios values (?,?,?)", usuarios)

# Recuperar varios registros
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

# print(usuarios)

for usuario in usuarios:
 print(usuario[0]," con el correo: ", usuario[2])

conexion.commit()

# Cerramos la conexion
conexion.close()