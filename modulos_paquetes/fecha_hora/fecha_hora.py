# importamos
from datetime import *

# Ahora, fecha del momento
dt = datetime.now()
# print(dt)

# print()

# print(dt.year)
# print(dt.month)
# print(dt.day)
# print()
# print(dt.hour)
# print(dt.minute)
# print(dt.second)
# print(dt.microsecond)

print()

# Crear una fecha
# dt = datetime(2000,1,1)
# print(dt)

# Esto es como una tupla, no se puede reescribir

# formateo en ISO
# print(dt.isoformat())

# Establecemos fecha horaria
import locale
locale.setlocale(locale.LC_ALL, 'es-ES')


# formatear a nuestro antojo
print(dt.strftime("%A %d de %B del %Y - %H:%M"))

import pytz
# Saber la hora en tokio
dtk = datetime.now(pytz.timezone('Asia/Tokyo'))


# Zona horaria
# dt.tzinfo