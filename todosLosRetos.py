#Creado por Leonardo Fariña y Mario Lara
#Creación: 15/03/2020 16:00 pm
#Modificación: 15/03/2020 16:30pm
#Versión: 3.8.2

#Importación de librerias

from miLibreriaRetos1 import *

#Definición de funciones

#Programa Principal

#Entradas
num1=(input("Escriba el número para ver la magia: "))
num2=(input("Escriba el siguiente numero para ver la magia: "))
num3=(input("Escriba el último numero para ver la magia: "))
num0=(input("Escriba el número para ver la magia (se recomiendan numeros menores a 5000): "))

#Salidas
print('Reto 1 formarNumeroInverso' , formarNumInvValid(num1,num2,num3))
print('Reto 2 obtenerPares' , obtenerParValid (num0))
print('Reto 3 obtenerfactorial' , obtenerFacValid(num0))
print('Reto 4\n(N°Pares,N°Impares) \n',obtenerCantValid (num0))
print('Reto 5 obtenerSumatoria' , obtenerSumValid (num0))
print('Reto 6 convertirABinario' , convertirABinValid (num0))
print('Reto 7 invertirNúmero' , invertirNumValid (num0))




  
