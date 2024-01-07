import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

# Clave primaria, identificador unico
# Consulta multilinia
cursor.execute('''
 CREATE TABLE usuarios(
 dni varchar(9) PRIMARY KEY,
 nombre varchar(100),
 edad int,
 email varchar(100)
 )
 ''')

usuarios = [
 ('1111111A','Hector', 19, 'hector@correo.com'),
 ('2222222B','Mario', 51, 'mario@correo.com'),
 ('3333333C','Mercedes', 38, 'mercedes@correo.com'),
 ('4444444D','Juan', 19, 'juan@correo.com')
]

cursor.executemany("INSERT INTO usuarios values (?,?,?,?)", usuarios)

# Creamos otra tabla 
cursor.execute('''
 CREATE TABLE productos (
 id integer PRIMARY KEY AUTOINCREMENT,
 nombre varchar(100) NOT NULL,
 marca varchar(50) NOT NULL,
 precio floar NOT NULL
 )
 ''')

# productos = [
#  ('Teclado', 'Logitech', 19.95),
#  ('Pantalla 19', 'LG', 89.95) 
# ]

# Se hace el insert de toda la vida

# Para el UNIQUE tiene la misma logica de siempre

# cursor.execute('''
#  CREATE TABLE productos (
#  id integer PRIMARY KEY AUTOINCREMENT,
#  nombre varchar(100) UNIQUE,
#  marca varchar(50) NOT NULL,
#  precio floar NOT NULL
#  )
#  ''')

# cuando es autoincrementado se deja asi: values(null, ?, ?, ?)

conexion.commit()
conexion.close()