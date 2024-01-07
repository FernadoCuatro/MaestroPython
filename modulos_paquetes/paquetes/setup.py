from setuptools import setup

setup(
	name         = "paquete",
	version      = "0.1",
	description  = "Este es un paquete de de ejemplo",
	author       = "Fernando Cuatro",
	author_email = "fernandocuatrorivera@gmail.com",
	url          = "https://google.com",
	script       = [],
	packages     = ["paquete", "paquete.adios", "paquete.hola"]
)
