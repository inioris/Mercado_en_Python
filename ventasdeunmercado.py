platanos = 100
guineos = 100
batata = 100
yuca = 100

def Bienvenida():
	print("Bienvenido al Sistema de Comprar Productos")
	print("Precione 1 Para ver la Lista de Productos Disponibles")
	print("Preciones 2 Para Comprar Productos")
	print("Precione 3 Para Avastecer Los Productos")
	print("Precione 4 Para Salir")

def ComprarPlatanos():
	global platanos
	print("Cuantos Platanos Decea Comprar")
	print("Tenga en Cuenta que solo Hay", platanos)
	comprar = int(input("Cantidad que Solicita >> "))
	if comprar > platanos :
		print("Su Pedido Sobrepasa La Cantidad Existente")
	else:
		platanos = platanos - comprar
		print(comprar, "Esta Fue la Cantidad de Yuca que Compro"))
	print("Platanos Disponibles", platanos)
	print("Gracias Por su Compra")

def ComprarGuineos():
	global guineos
	print("Cuantos Guineos Decea Comprar")
	print("Tenga en Cuenta que solo Hay", guineos)
	comprar = int(input("Cantidad que Solicita >> "))
	if comprar > guineos :
		print("Su Pedido Sobrepasa La Cantidad Existente")
	else:
		guineos = guineos - comprar
		print(comprar, "Esta Fue la Cantidad de Yuca que Compro")
	print("Guineos Disponibles", guineos)
	print("Gracias Por su Compra")

def ComprarBatata():
	global batata
	print("Que Cantidad de Batatas Decea Comprar")
	print("Tenga en Cuenta que solo Hay", batata)
	comprar = int(input("Cantidad que Solicita >> "))
	if comprar > batata :
		print("Su Pedido Sobrepasa La Cantidad Existente")
	else:
		batata = batata - comprar
		print(comprar, "Esta Fue la Cantidad de Yuca que Compro")
	print("Batatas Disponibles", batata)
	print("Gracias Por su Compra")

def ComprarYuca():
	global yuca
	print("Que Cantidad de Yuca Decea Comprar")
	print("Tenga en Cuenta que solo Hay", yuca)
	comprar = int(input("Cantidad que Solicita >> "))
	if comprar > yuca :
		print("Su Pedido Sobrepasa La Cantidad Existente")
	else:
		yuca = yuca - comprar
		print(comprar, "Esta Fue la Cantidad de Yuca que Compro")
	print("Yuca Disponibles", yuca)
	print("Gracias Por su Compra")

def Cantidad():
	global platanos
	global guineos
	global batata
	global yuca
	print("Cantidad de Platanos Disponibles >> ",platanos)
	print("Cantidad de Guineos Disponibles >> ",guineos)
	print("Cantidad de Batatas Disponibles >> ",batata)
	print("Cantidad de Yuca Disponibles >> ",yuca)

# Funciones de Avastecimiento 
def AvastecerPlatanos():
	global platanos
	print("Cantidad de Platanos Disponibles >> ",platanos)
	Avastecer = int(input("Cantidad de Platanos que Decea Avastecer >> "))
	platanos = platanos + Avastecer

def AvastecerGuineos():
	global guineos
	print("Cantidad de Guineos Disponibles >> ",guineos)
	Avastecer = int(input("Cantidad de Guineos que Decea Avastecer >> "))
	guineos = guineos + Avastecer

def AvastecerBatata():
	global batata
	print("Cantidad de Batatas Disponibles >> ",batata)
	Avastecer = int(input("Cantidad de Batatas que Decea Avastecer >> "))
	batata = batata + Avastecer

def AvastecerYuca():
	global yuca
	print("Cantidad de Yuca Disponibles >> ",yuca)
	Avastecer = int(input("Cantidad de Yuca que Decea Avastecer >> "))
	yuca = yuca + Avastecer


def AvastecerMercado():
	global platanos
	global guineos
	global batata
	global yuca
	print("Precione 1 Para Avastecer Platanos")
	print("Precione 2 Para Avastecer Guineos")
	print("Precione 3 Para Avastecer Batata")
	print("Precione 4 Para Avastecer Yuca")
	opcion = input("Introdusca su Opcion >> ")

def Comprar():
	global platanos
	global guineos
	global batata
	global yuca
	print("Precione 1 Si Decea Comprar Platanos")
	print("Precione 2 Si Decea Comprar Guineos")
	print("Precione 3 Si Decea Comprar Batata")
	print("Precione 4 Si Decea Comprar Yuca")
	opcion = input("Introdusca su Opcion >> ")
	if opcion == "1":
		ComprarPlatanos()
	if opcion == "2":
		ComprarGuineos()
	if opcion == "3":
		ComprarBatata()
	if opcion == "4":
		ComprarYuca()
	else:
		print("No Hay mas Opciones Disponibles")


salir = "2"
while salir != "1":
	Bienvenida()
	opciones = input("Introdusca su Opcion >> ")
	if opciones == "1":
		Cantidad()
	if opciones == "2":
		Comprar()
	if opciones == "3":
		AvastecerMercado()
	if opciones == "4":
		Comprar()
	else:
		print("No Hay mas Opciones Disponibles")
	salir = input("Para Salir Precione 1 Para continuar Cualiquier Tecla >> ")
	