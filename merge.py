#Creado por Mario Lara,Diego Alvarez,Raul Sanabria, Gilberth Rogriguez
#Este codigo fue creado por Mohit Kumra 
#Fecha de Creación:27/05/2020
#Última modificación:28/05/2020
#Versión 3.8.3
# Importación de libreria
import random
#Definición de funciones
# Programa de python implementación del Orden por Mezcla
# Mezcla dos sublistas de la lista[]. 
# La primer sublista es lista[izquierda..medio] 
# La segunda sublista es lista[medio+1..derecha] 
def mezcla(lista, izquierda, medio, derecha): 
    n1 = medio - izquierda + 1 
    n2 = derecha - medio 
    # crea listas temporales 
    IZQ = [0] * (n1) 
    DER = [0] * (n2) 
    # Copia datos a las listas temporales IZQ[] y DER[] 
    for i in range(0 , n1): 
        IZQ[i] = lista[izquierda + i] 
    for j in range(0 , n2): 
        DER[j] = lista[medio + 1 + j] 
    # Une las listas temporales en una sola lista [izquierda..derecha] 
    i = 0     # Indice inicial de la primer sublista
    j = 0     # Indice inicial de la segunda sublista
    k = izquierda     # Indice inicial de la tercera sublista
    while i < n1 and j < n2 :   
        if IZQ[i] <= DER[j]: 
            lista[k] = IZQ[i] 
            i += 1
        else: 
            lista[k] = DER[j] 
            j += 1
        k += 1
    # Copia los elementos restantes de IZQ[], si hay alguno 
    while i < n1: 
        lista[k] = IZQ[i] 
        i += 1
        k += 1
    # Copia los elementos restantes de DER[], si hay alguno  
    while j < n2: 
        lista[k] = DER[j] 
        j += 1
        k += 1
# izquierda is es de "indice izquierdo" y derecha de "indice derecho" de la
# sublista de la lista que será ordenada
def ordenMezcla(lista,izquierda,derecha): 
    if izquierda < derecha: 
        # Es lo mismo que (izquierda+derecha)//2, pero evita el overflow del 
        # large izquierda and h 
        medio = (izquierda+(derecha-1))//2
        # Ordena la primera y la segunda mitad 
        ordenMezcla(lista, izquierda, medio) 
        ordenMezcla(lista, medio+1, derecha) 
        mezcla(lista, izquierda, medio, derecha) 
#Genera una lista de números al azar  
def listaRandom(num):
    lista=[]
    i=1
    while i<=num:
        rand=random.randint(0,100)
        lista+=[rand]
        i+=1
    return lista
# Codigo Piloto para hacer las pruebas
#Programa Principal
numero = int(input("Ingrese la cantidad de elementos que quiere para su lista: "))
lista = listaRandom(numero)
n = len(lista) 
print ("La lista es: ")
print(lista)
ordenMezcla(lista,0,n-1)
print ("\n\nLista Ordenada") 
print (lista) 
#Este codigo fue creado por Mohit Kumra 
