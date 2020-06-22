#Creado por: Gilbert Rodríguez Mejias
#Fecha de creación: 05/20/2020 1:35p.m
#Última modificacion: 05/20/2020 p.m
#Version 3.8.1

#Importacion de librerias

#Funciones 
def obtenerInformacion(palab):
	"""
	funcionalidad: separar las palabras de un string
	Entradas:
	-palab: la lista de la funcion decodificar
	Salidas:
	- lista
	"""
	persona=palab.split("°")
	persona=persona[0].split(";")+persona[1:]
	return persona


def decodificar(plista):
	"""
	funcionalidad: obtener una lista del codigo ingresado
	Entradas:
	-palab: el string ingresado por el usuario
	Salidas:
	- lista
	"""

	lista=[]
	codigo=plista.split("^")
	for i in range(len(codigo)):
		lista+=obtenerInformacion(codigo[i])
	return lista


def saberGenero(palab):
	"""
	funcionalidad: obtener el genero de la persona
	Entradas:
	-palab: la letra correspondiente al genero
	Salidas:
	-Un string correspondiente al genero
	"""
	if palab.strip()=="F":
		return "Femenino"
	return "Masculino"


def contarGenero(lista):
	"""
	funcionalidad: obtener la cantidad de hombres y mujeres
	Entradas:
	-palab: la lista completa
	Salidas:
	-Femenino: cantidad de mujeres
	-Masculino: cantidad de hombres
	"""
	femenino=0
	masculino=0
	for i in range(len(lista)):
		if lista[i].strip() =="F":
			femenino+=1
		elif lista[i].strip() =="M":
			masculino+=1
	return femenino,masculino


def contarPersonas(lista):
	"""
	funcionalidad: obtener la cantidad de personas por provincia
	-palab: la lista completa
	Salidas:
	-la cantidad de personas por provincia
	"""
	sanJose=0
	alajuela=0
	cartago=0
	heredia=0
	guanacaste=0
	puntarenas=0
	limon=0
	for i in range(len(lista)):
		if not lista[i].strip().isalnum():
			if lista[i][0]=="1":
				sanJose+=1
			if lista[i][0]=="2":
				alajuela+=1
			if lista[i][0]=="3":
				cartago+=1
			if lista[i][0]=="4":
				heredia+=1
			if lista[i][0]=="5":
				guanacaste+=1
			if lista[i][0]=="6":
				puntarenas+=1
			if lista[i][0]=="7":
				limon+=1

	return sanJose,alajuela,cartago,heredia,guanacaste,puntarenas,limon


def ordenarDatos(plista):
	"""
	funcionalidad: ordenar los resultados de la decodificacion del string
	-palab: el string codificado
	Salidas:
	-nombre,apellido1,apellido2,cedula,sexo: estos datos uno a uno por persona en la lista
	-cantidad hambres y mujeres: correspondientes al string ingresado
	-cantidad de personas por provincia
	"""
	lista=decodificar(plista)
	femenino,masculino=contarGenero(lista)
	provincias=contarPersonas(lista)
	i=0
	while i < len(lista):
		print("Nombre completo: ",lista[i],lista[i+1],lista[i+2],
			"\nCédula: ",lista[i+3],"\nSexo: ",saberGenero(lista[i+4]))
		i+=5

	print("\nEstadísticas de: \nCantidad de mujeres: ",femenino,
		"\nCantidad de hombres: ",masculino,"\nPersonas por provincia: ",
		"\nSan José: ",provincias[0],"\nAlajuela: ",provincias[1],
		"\nCartago: ",provincias[2],"\nHeredia: ",provincias[3],
		"\nGuanacaste: ",provincias[4],"\nPuntarenas: ",provincias[5],
		"\nLimón: ",provincias[6],)

#Programa principal

palabra="Ana;Mora;Tencio°3-3456-0987°F ^Juan;Arias;Quirós°1-0654-1345°M ^Enrique;Miranda;Ortega°5-6547-8745°M ^María;Montero;Fonseca°1-6654-7458°F ^Angela;Montero;Fonseca°2-6654-7458°F ^Gilbert;Rodríguez;Mejias°2-0826-0296°M"
ordenarDatos(palabra)
 
