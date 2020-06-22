#Creado por: Gilbert Rodríguez Mejias y Raúl Sanabria Marroquín
#Fecha de creación: 03/06/2020 2:00p.m
#Última modificacion: /05/2020 p.m
#Version 3.8.1

#Importacion de librerias
import re
#Varables globales
global recuperadosDonantes

recuperadosDonantes=["303500620","101110218","412340987","267893456","154328765","534561234",
"187674329","265437654","243214321","187654321","187659870","687659870","887659870",
"945659823"]
global provincia
provincia=["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón","nacionalizados o naturalizados","partida especial de nacimientos"]
#Definicion de funciones
#▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅ Reto 1 ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅#
def pedirCedula():
	"""
	funcionalidad: pedirle al usuario que ingrese una cedula, ademas verifica que la cedula 
	sea correcta e insistir hasta que la cedula ingresada correctamente.
	Entradas:
	-cedula: le pide al usuario por consola que ingrese una cedula.
	Salidas:
	-cedula: la cedula correcta'
	-un print si la cedula ingresada esta incorrecta, diciendole al usuario que 
	la cedula esta ingresada incorrectamente y ademas le da un ejemplo.
	"""
	while True:
		cedula=input("Ingrese la cédula: ")
		if re.match(r"^([1-9])\d{8}$", cedula):
			return cedula
		else:
			print("cédula ingresada incorrectamente.Ejemplo correcto: 101110218")

def agregarDonantes(num):
	"""
	funcionalidad: pedir una a una las cedulas que el usuario dijo que iba a ingresar y 
	tambien agregarlas a una lista global si aun la cedula no esta en esa lista.
	Entradas:
	-num: el numero de cedulas que va a ingresar el usuario.
	Salidas:
	-la lista modificada con las nuevas cedulas que se le agregaron.
	"""
	contador=0
	while contador<num:
		cedula=pedirCedula()
		if cedula not in recuperadosDonantes:
			recuperadosDonantes.append(cedula)
			print("La cédula fue registrada correctamente.")
			contador+=1
		elif cedula in recuperadosDonantes:
			print("La cédula ya a sido registrada con anterioridad. Registre una nueva cédula.")
		print("A ingresado ",contador," cédulas nuevas.")

	return ""
#▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅ Reto 2 ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅#
def decodificarDonador(cedula):
	"""
        Funcionalidad: Esta función decodifica la cedula introducida por el usuario.
        Entradas:
        -cedula: le pide al usuario por consola que ingrese una cedula.
        Salidas:
        - La información decodificada proveniente de la cedula.
        """
	if cedula in recuperadosDonantes:
		if 1 <= int(cedula[0]) <= 7 :
			print("Usted en la provincia de: nació ",provincia[int(cedula[0])-1],", en el tomo ",cedula[1:5]," y el asiento"," ",cedula[5:])
		elif int(cedula[0])==8:
			print("Usted es",provincia[int(cedula[0])-1],", en el tomo ",cedula[1:5]," y el asiento ",cedula[5:])
		elif int(cedula[0])==9:
			print("Usted es de",provincia[int(cedula[0])-1],", en el tomo ",cedula[1:5]," y el asiento ",cedula[5:])
	else:
		print("El donador no es un donante aún")
	return ""

#▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅ Reto 3 ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅#
def listarDonantes(num):
	"""
	funcionalidad: optener de listaCedulas las listas que empiecen por el num ingresado
	Entradas:
	-num: referente al lugar de procedencia de los donantes que se desean buscar en lista
	Salidas:
	-printea las cedulas que empiezan con el num ingresado
	"""
	for i in recuperadosDonantes:
		if i[0]==num:
			print(i)
	return ""

#▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅ Reto 4 ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅#
def obtenerCantidad(num):
	"""
        Funcionalidad: Obtiene la cantidad de cedulas que hay en la provincia deseada.
        Entradas:
        -num: Numero que representa el primer digito de la cedula y este nos dice el origen 
        de procedencia 
        Salidas:
        - La cantidad de cedulas en la provincia
        """
	cant = 0
	for i in recuperadosDonantes:
		if i[0] == num:
			cant += 1
	return cant

def cedulasTotales():
    """"
    Funcionalidad: Esta funcion nos da todos los donantes que hay en una provincia 
    y si no hay nos indica que no se han reportado donantes.
    Entradas:
    -num: El numero que nos indica de cual provincia se quiere saber el total de cedulas.
    Salidas:
    - La cantidad de cedulas de donadores de la provincia mas las cedulas en si  impresas 
    de forma vertical.
    """
    num=1
    while num<=9:
	    if 1 <= num <= 7 :
	        print("Los donadores de la provincia de",provincia[num-1]," son ",obtenerCantidad(str(num)),"con la cédulas:")
	        if obtenerCantidad(str(num)) == 0:
	            print("Aún no reporta donadores")
	        print(listarDonantes(str(num)))
	    elif num == 8:
	        print("Los donadores",provincia[num-1]," son ",obtenerCantidad(str(num)),"con la cédulas:")
	        if obtenerCantidad(str(num)) == 0:
	            print("Aún no reporta donadores")
	        print(listarDonantes(str(num)))
	    elif num == 9:
	        print("Los donadores de",provincia[num-1]," son ",obtenerCantidad(str(num)),"con la cédulas:")
	        if obtenerCantidad(str(num)) == 0:
	            print("Aún no reporta donadores")
	        print(listarDonantes(str(num)))
	    num+=1
    return ""
#▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅ Reto 5 ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅#
def obtenerDonadoresExtranjeros(num):
	"""
    Funcionalidad: Esta funcion nos da todos los donantes que son nacionalizados o de partida
    especial y si no hay nos indica que no se han reportado donantes.
    Entradas:
    -num: El numero que nos indica de cual de las dos si nacionalizados o partida especial.
    Salidas:
    - La cantidad de cedulas de donadores que son nacionalizados o de partida especial mas 
    las cedulas en si  impresas de forma vertical.
    """
	if num == 1:
		print("Los donadores",provincia[7]," son ",obtenerCantidad(str(8)),"con la cédulas:")
		if obtenerCantidad(str(8)) == 0:
			print("Aún no reporta donadores")
		listarDonantes(str(8))
	elif num == 2:
		print("Los donadores de",provincia[8]," son ",obtenerCantidad(str(9)),"con la cédulas:")
		if obtenerCantidad(str(9)) == 0:
			print("Aún no reporta donadores")
		listarDonantes(str(9))
	return ""




#Programa principal

