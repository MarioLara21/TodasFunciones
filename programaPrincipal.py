#Creado por: Gilbert Rodríguez Mejias y Raúl Sanabria Marroquín
#Fecha de creación: 27/05/2020 6:30p.m
#Última modificacion: /05/2020 p.m
#Version 3.8.1

#Importacion de librerias
import re

#Definicion de funciones 
#-------------------------------Reto 2-------------------------------#
def positivosNegativos(lista):


	positivos=[]
	negativos=[]
	for i in range(len(lista)):
		if lista[i]>=0:
			positivos.append(lista[i])
		elif lista[i]<0:
			negativos.append(lista[i])
	return[positivos,negativos]

def positivosNegativosAux(lista):
	"""
	funcionalidad: validar los datos de la funcion positivosNegativos(lista)
	Entradas:
	-lista: la lista que ingresa el usuario
	Salidas:
	-True si los datos ingresados estan bien
	-False si los datos ingresados estan incorrectos
	-un print diciendo cual es le error en los datos ingresados 
	"""
	if not isinstance(lista,list):
		print("Debe de ser una lista.")
	else:
		return True
	return False

def mostrarPositivosNegativos(lista):
	"""
	funcionalidad: optener las entradas y mostrar a la funcion buscarElemento
	Entradas:
	-lista: la lista que ingresa el usuario
	-elem: numero(int) que se debe de buscar en la lista
	Salidas:
	-la funcion buscarElemento
	"""
	validar=False
	while True:
		try:
			validar=positivosNegativosAux(lista)
			break
		except:
			print("Un error en los datos ingresados, el dato debe de ser un nuemro entero")
			break
	if validar==False:
		return""
	print(positivosNegativos(lista))
	return""

#-------------------------------Reto 4-------------------------------#
def separaNumeros(lista):
	"""
	funcionalidad: separar un numero en elementos que formaran un nueva lista
	-num: numero(int) que se desea separar en elementos, y almacenar en una lista
	Salidas:
	-una nueva lista con los elementos del numero
	"""
	nuevaLista=[]
	while lista!=0:
		nuevaLista.append(lista%10)
		lista//=10
	return nuevaLista

def agrupar(lista):
	"""
	funcionalidad: agrupar los numeros de una lista, esto cuando son iguales
	entradas:
	-lista: con los elementos de un numero separados en una lista
	Salidas:
	-una lista con un numero con sus elementos acomodados en orden
	"""
	lista1=[]
	listaFinal=[]
	for i in range(len(lista)):
		lista1+=[separaNumeros(lista[i])]

	for i in range(len(lista1)):
		num=0
		listaImag=lista1[i]
		elevar=len(listaImag)-1
		for j in range(len(listaImag)):
			indice=0
			contador=len(listaImag)
			if listaImag==[]:
				break
			comparador=listaImag[-1]
			while contador!=0:
				if listaImag[indice]==comparador:
					num+=(listaImag.pop(indice))*(10**elevar)
					indice-=1
					elevar-=1
				contador-=1
				indice+=1
		listaFinal+=[num]

	return listaFinal

def agruparAux(lista):
	"""
	funcionalidad: validar los datos de la funcion agrupar(lista)
	Entradas:
	-lista: la lista que ingresa el usuario
	Salidas:
	-True si los datos ingresados estan bien
	-False si los datos ingresados estan incorrectos
	-un print diciendo cual es le error en los datos ingresados 
	"""
	if not isinstance(lista,list):
		print("Debe de ser una lista.")
		return False
	for i in lista:
		if not isinstance(i,int):
			print("Deben de ser numeros enteros los elementos de la lista.")
			return False
		elif i<0:
			print("Deben de ser números enteros positivos.")
			return False
	return True

def mostrarAgrupar(lista):
	"""
	funcionalidad: optener las entradas y mostrar a la funcion agrupar
	Entradas:
	-lista: la lista que ingresa el usuario
	-elem: numero(int) que se debe de buscar en la lista
	Salidas:
	-la funcion agrupar
	"""
	validar=False
	while True:
		try:
			validar=agruparAux(lista)
			break
		except:
			print("Un error en los datos ingresados, el dato debe de ser una lista")
			break
	if validar==False:
		return""
	print(agrupar(lista))
	return""

#-------------------------------Reto 6-------------------------------#

def listaNumeros(lista):
	num2=[]
	num=re.findall(r"[-+]?\d*\.\d+|\d+",lista)
	for i in num:
		try:
			num2+=[int(i)]
		except:
			num2+=[float(i)]
	return num2

def listaNumerosAux(lista):
	"""
	funcionalidad: validar los datos de la funcion agrupar(lista)
	Entradas:
	-lista: la lista que ingresa el usuario
	Salidas:
	-True si los datos ingresados estan bien
	-False si los datos ingresados estan incorrectos
	-un print diciendo cual es le error en los datos ingresados 
	"""
	if not isinstance(lista,str):
		print("Debe de ser un str.")
	else:
		return True
	return False

def mostrarListaNumeros(lista):
	"""
	funcionalidad: optener las entradas y mostrar a la funcion agrupar
	Entradas:
	-lista: la lista que ingresa el usuario
	-elem: numero(int) que se debe de buscar en la lista
	Salidas:
	-la funcion agrupar
	"""
	validar=False
	while True:
		try:
			validar=listaNumerosAux(lista)
			break
		except:
			print("Un error en los datos ingresados, el dato debe de ser un string.")
			break
	if validar==False:
		return""
	print(listaNumeros(lista))
	return""

#Programa principal
#-------------------------------Reto 2-------------------------------#

print("\nReto 2")
print("\nEjemplo 1")
mostrarPositivosNegativos([4, -1, 2, 8, -4, -2])
print("\nEjemplo 2")
mostrarPositivosNegativos([-1, -4, -2])

#-------------------------------Reto 4-------------------------------#

print("\nReto 4")
print("\nEjemplo 1")
mostrarAgrupar( [20845224809, 213323])
print("\nEjemplo 2")
mostrarAgrupar([])

#-------------------------------Reto 6-------------------------------#
print("\nReto 6")
print("\nEjemplo 1")
mostrarListaNumeros("xy225p30ab0g8.9iou1000")

print("\nEjemplo 2")
mostrarListaNumeros("ab95.8124c76n")

print("\nEjemplo 3")
mostrarListaNumeros("x0.25za10.5")

print("\nEjemplo 4")
mostrarListaNumeros("xyz")



