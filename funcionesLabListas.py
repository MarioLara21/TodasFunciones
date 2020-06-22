#Creado por: Gilbert Rodríguez Mejias y Raúl Sanabria Marroquín
#Fecha de creación: 22/05/2020 1:00p.m
#Última modificacion: 22/05/2020 p.m
#Version 3.8.1

#Importacion de librerias
import random

#Funciones
#--------------------------------------Reto 2-------------------------------------# 
def buscarElemento (lista,elem):
	"""
	funcionalidad: determinr cuantas veces aparece un numero en una lista
	Entradas:
	-lista: la lista que ingresa el usuario
	-elem: numero(int) que se debe de buscar en la lista
	Salidas:
	- un numero(int)
	"""
	total=0
	for i in range(len(lista)):
		if lista[i]==elem:
			total+=1
	print(total)
	return""

#--------------------------------------Reto 4-------------------------------------# 
def crearLista(num):
	"""
	funcionalidad: recibir un numero del cual se hara una lista de numeros 
	random y sacar el numero mayor, el numero menor y la diferencia
	Entradas:
	-num: numero(int) del cual se especifica el largo de la lista
	Salidas:
	-mayor: el numero mayor de una serie de numeros random
	-menor: el numero menor de una serie de numeros random
	-diferencia: la diferencia entre el mayor y el menor
	"""
	lista=[]
	i=1
	while i<=num:
		rand=random.randint(1, 99)
		lista+=[rand]
		i+=1
	return lista

#--------------------------------------Reto 6-------------------------------------# 
def eliminarRepetidos(lista):
	"""
	funcionalidad: crear una nueva lista donde no se repiten elementos iguales
	Entradas:
	-lista: la lista que se debe de analizar
	Salidas:
	-una nueva lista sin elementos repetidos
	"""
	listaNueva=[]
	for i in range(len(lista)):
		if lista[i] not in listaNueva:
			listaNueva+=[lista[i]]
	return listaNueva

#--------------------------------------Reto 8-------------------------------------# 
def alternar(lista):
	"""
	funcionalidad: identificar si en una lista los numeros estan alternados o no
	Entradas:
	-lista: la lista que se debe de analizar
	Salidas:
	-una nueva lista sin elementos repetidos
	"""
	valor=""
	lista1=lista[1::2]
	lista2=lista[0::2]
	for i in lista:
		if (lista[0]%2==0):
			for i in range(len(lista1)):
				if (lista1[i]%2!=0):
					for i in range(len(lista2)):
						if (lista2[i]%2==0):
							valor=True
						else:
							valor=False
				else:
					valor=False
		elif (lista[0]%2!=0):
			for i in range(len(lista1)):
				if (lista1[i]%2==0):
					for i in range(len(lista2)):
						if (lista2[i]%2!=0):
							valor=True
						else:
							valor=False
				else:
					valor=False
	return valor

#--------------------------------------Reto 10-------------------------------------#
def replicar(lista,mult):
	"""
	funcionalidad: crear una nueva lista donde se repliquen 
	los elementos de la lista inicial
	Entradas:
	-lista: la lista que se debe de analizar
	-mult: la cantidad de veces que se deben de replicar los elemntos de la lista
	Salidas:
	-una nueva lista con los elementos replicados de la lista inicial
	"""
	nuevalista=[]
	for i in range(len(lista)):
		nuevalista+=[lista[i]]*mult
	return nuevalista

#--------------------------------------Reto 12-------------------------------------#
def unirConjuntos(lista1,lista2):
	"""
	funcionalidad: crear una nueva lista donde se unan dos listan sin los numeros
	repetidos
	Entradas:
	-lista1: la lista que se debe de unir
	-lista2: la lista que se debe de unir
	Salidas:
	-una nueva lista 
	"""	
	nuevalista=[]
	nuevalista+=eliminarRepetidos(lista1)+eliminarRepetidos(lista2)
	nuevalista=eliminarRepetidos(nuevalista)
	return nuevalista


#--------------------------------------Reto 14-------------------------------------#
def multiplicarLista(lista1,lista2):
	"""
	funcionalidad: crear una nueva lista donde se multipliquen 
	los elementos de las dos listaas entre si, el primer elemento de la lista1
	con el primer elemento de la lista2 y asi sucesivamente 
	Entradas:
	-lista1: la lista que se debe de analizar
	-lista2: la lista que se debe de analizar
	Salidas:
	-una nueva lista con los elementos multiplicados de cada lista
	"""
	nuevalista=[]
	for i in range(len(lista1)):
		nuevalista+=[lista1[i]*lista2[i]]
	return nuevalista





#Programa principal

