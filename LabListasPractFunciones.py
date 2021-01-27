#Creado por Mario Lara Molina y Leonardo Fariña
#Fecha de creación:22/05/2020 10:48 am
#Última modificación: 23/05/2020
#Versión 3.8.3
#Importación de librerias

from LabListasPractFunciones import *
import random

#Def de variables
lista=["x",236.6,"e","b",3,"a",3j]
lista2=[11, 45, 89, -6, 0, 78, 45, 156, 12]
lista3=[2,3,4,5,6]
lis=[1,3,3,7]
numero=5

#Def de funciones
###RETO1#################################################################################
def validarSepararElementos(lis):
    """
    Funcionalidad:Validar los datos para la función separarElementos
    Entradas:lis(lista)
    Salidas:Datos validados 
    """
    try:
        lis = int(lis)
        assert lis != []
        
        return separarElementos(lis)
        
    except AssertionError:
        print("La lista de números no debe ser vacía")
                
    except ValueError:
        print("Elementos no numéricos en la lista")
    except:
        print("Llame al programador")
        
def mostrarSepararElementos():
    """
    Funcionalidad:Mostrar en pantalla la función susecionUlam
    Salidas:Datos en pantalla
    """
    lista=[1,2,3,4,5,6,7,8]
    print("La lista a usar es: ", lista)
    par,impar = separarElementos(lista)
    print("Los pares son: ", par," y los impares son: ", impar)


###RETO2#################################################################################
def validarElemento(lista2=None,elemento=None):
    """
    Funcionalidad:Validar los datos de la función buscarElemento
    Entradas:lista2(Lista con valores enteros), elemento(int,número a buscar en la lista=
    Salidas:Valores validados
    """
    try:
        if lista2==None:
            return "Debe ingresar una lista con valores enteros"
        elif elemento==None:
            return "Debe indicar el número que desea buscar"
        
        for i in lista2:
            if not isinstance(i,int):
                return "Debe ingresar solamente valores numéricos enteros"
        return buscarElemento(lista2,elemento)
    except ValueError:
        print("Ingrese un valor válido")
    except:
        print("Llame al programador")
def mostrarBuscarElemento():
    """
    Funcionalidad:Mostrar los datos de buscarElemento
    Salidas: Datos en pantalla
    """
    lista2 = [2,4,5,6,7,2,2,2,2]
    elemento = 2
    print("Lista a usar: ",lista2,"El ",elemento,"se repitio :",validarElemento(lista2, elemento)," veces.")
    
###RETO3#################################################################
def validarListaVocales(lista):
    """
    Funcionalidad: Validar los datos 
    Entradas: Lista(list)
    Salidas:Datos validados para la función de proceso
    """
    try:
        validado=[]
        for i in lista:
            if isinstance(i,str):
                validado.append(i)
            else:
                return "Debe ingresar solamente letras"

        return crearListaVocales(validado)
    except ValueError:
        print("Debe ingresar una lista")
    except:
        print("Llame al programador")
        
def mostrarListaVocales():
    """
    Funcionalidad:Mostrar los datos de crearListaVocales
    Salidas: Datos en pantalla
    """
    print(validarListaVocales(lista))
####RETO4##################################################################
def validarLista(numero):
    """
    Funcionalidad:Validar los datos para la función crearLista
    Entradas:numero(int)=Cantidad de elementos en la lista
    Salidas:Datos validados 
    """
    try:
        if not isinstance(numero,int):
            print ("Debe ingresar un contador de tipo entero")
        elif numero<0:
            print("El contador debe ser mayor a cero")
        else:
            return crearLista(numero)
            
    except ValueError:
        print("Debe ingresar un contador de tipo entero")
    except:
        print("Llame al programador")

def mostrarLista():
    """
    Funcionalidad:Mostrar en pantalla la función crearLista
    Salidas:Datos en pantalla
    """
    numero=5
    mayor,menor,lista=crearLista(numero)
    print("Se generó la lista",lista,"el mayor es:",mayor,"el menor es:",menor,"hay una diferencia de:",mayor-menor)

#####RETO5#####################################################################
def validarInsertarElemento(elemento1,elemento2,lista):
    """
    Funcionalidad: Valida los datos de la función insertarElemento
    Entradas:Lista(list)
    Salidas: Datos validados
    """
    try:
        for i in lista:
            if not isinstance(i,int):
                print("Los valores de la lista deben ser enteros")
            elif i<0:
                print("Los elementos de la lista deben ser mayores a cero")
        return insertarElemento(elemento1,elemento2,lista)
    except ValueError:

                print("Debe ingresar una lista")
    except:
        print("Llame al programador")
def mostrarListaAscendente():
    """
    Funcionalidad:Mostrar en pantalla la función listaAscendente(lista)
    Salidas:Datos en pantalla
    """
    print("Nuestro elemento 1 es: ",elemento1," \n Nuestro elemento 2 es: ",elemento2,"\n Nuestra lista es: ",lista)
    print("El resultado es: ",validarInsertarElemento(elemento1,elemento2,lista))
    validarAscendente(lista)
###RETO6#################################################################################

def validarEliminarElementosRepetidos(lista):
    """
    Funcionalidad: Valida los datos de la función EliminarElementosRepetidos
    Entradas:Lista(list)
    Salidas: Datos validados
    """
    try:
        for i in lista:
            if not isinstance(i,int):
                print("Los valores de la lista deben ser enteros")
            elif i<0:
                print("Los elementos de la lista deben ser mayores a cero")
        return eliminarElementosRepetidos(lista)
    except ValueError:
        print("Debe ingresar una lista")
    except:
        print("Llame al programador")
        
def mostrarEliminarElementosRepetidos():
    """
    Funcionalidad:Mostrar en pantalla la función listaAscendente(lista)
    Salidas:Datos en pantalla
    """
    lista= [1,2,3,4,5,6,7,8,9,3,4,5,1,2,1]
    print("Se usara la lista :",lista)
    print("El resultado es: ",validarEliminarElementosRepetidos(lista))


###RETO7#################################################################################
def validarsusecionUlam(numero):
        """
        Funcionalidad:Validar los datos para la función susecionUlam
        Entradas:numero(int)
        Salidas:Datos validados 
        """
        try:
            if not isinstance(numero,int):
                print ("Debe ingresar un contador de tipo entero")
            elif numero<0:
                print("El contador debe ser mayor a cero")
            else:
                return susecionUlam(numero)
                
        except ValueError:
            print("Debe ingresar un contador de tipo entero")
        except:
            print("Llame al programador")
def mostrarSusecionUlam():
    """
    Funcionalidad:Mostrar en pantalla la función susecionUlam
    Salidas:Datos en pantalla
    """
    numero=26
    print("El número a usar es: ",numero)
    print("Se generó la lista :",validarsusecionUlam(numero))
    
#####RETO8#####################################################################
def validarAlternativos(lista):
    """
    Funcionalidad: Valida los datos de la función Alternativos
    Entradas:Lista(list)
    Salidas: Datos validados
    """
    try:
        assert lista != []
        return alternativos(lista)
        
    except AssertionError:
        print("La lista de números no debe ser vacía")
    except ValueError:
        print("Debe ingresar una lista")
    except:
        print("Llame al programador")
        
def mostrarAlternativos():
    """
    Funcionalidad:Mostrar en pantalla la función Alternativos
    Salidas:Datos en pantalla
    """
    lista=[2,3,4,5,6]
    print("Lista usada: ", lista)
    print("Respuesta: ",validarAlternativos(lista))
    
#####RETO9#####################################################################
def validarAscendente(lista):
    """
    Funcionalidad: Valida los datos de la función listaAscendente
    Entradas:Lista(list)
    Salidas: Datos validados
    """
    try:
        for i in lista:
            if not isinstance(i,int):
                print("Los valores de la lista deben ser enteros")
            elif i<0:
                print("Los elementos de la lista deben ser mayores a cero")
        return listaAscendente(lista)
    except ValueError:
        print("Debe ingresar una lista")
    except:
        print("Llame al programador")
def mostrarListaAscendente():
    """
    Funcionalidad:Mostrar en pantalla la función listaAscendente(lista)
    Salidas:Datos en pantalla
    """
    lista3=[2,3,4,5,6]
    validarAscendente(lista)
####RETO10##############################################################################
def validarReplicar(lis,num):
    try:
        if lis==None:
            print("Debe ingresar una lista")
        elif num==None:
            print("Debe ingresar el número por el cual multiplicar la lista")
        if not isinstance(num,int):
            print("El número debe ser de tipo entero")
        elif num<0:
            print("El numero debe ser mayor a cero")
        for i in lis:
            if not isinstance(i,int):
                print("Los elementos de la lista deben ser números enteros")
        return replicar(lis,num) 
    except ValueError:
        print("Debe ingresar una lista y un número válidos")    
    except:
        print("Llame al programador")
def mostrarReplicar():
    """
    Funcionalidad:Mostrar en pantalla la función replicar(lis=None,num=None)
    Salidas:Datos en pantalla
    """
    lis = [1,2,3]
    num = 3
    print("Esta es la lista que vamos a usar:",lis,"y este es el número por el que vamos a multiplicar:",num)
    print("Resultado: ",validarReplicar(lis,num))

####RETO11##############################################################################
def validarDiferenciaConjuntos(lis,lis1):
    """
    Funcionalidad: Valida los datos de la función diferenciaConjuntos
    Entradas:lis(lista),lis1(lista)
    Salidas: Datos validados
    """
    try:
        for i in lis:
            if not isinstance(i,int):
                print("Los valores de la lista deben ser enteros")
            elif i<0:
                print("Los elementos de la lista deben ser mayores a cero")
        for l in lis1:
            if not isinstance(i,int):
                print("Los valores de la lista deben ser enteros")
            elif i<0:
                print("Los elementos de la lista deben ser mayores a cero")
        assert lis != [] or lis1 != []
        return diferenciaConjuntos(lis,lis1)
    
    except AssertionError:
        print("La lista de números no debe ser vacía")        
    except ValueError:
        print("Debe ingresar una lista")
    except:
        print("Llame al programador")

def mostrarDiferenciaConjuntos():
    """
    Funcionalidad:Mostrar en pantalla la función diferenciaConjuntos
    Salidas:Datos en pantalla
    """
    lista=[2,3,4,5,6]
    lista1=[1,4,5,8,9]
    print("A = ",lista,"\n B = ",lista1)
    print("A-B = ",validarDiferenciaConjuntos(lista,lista1))
####RETO12##############################################################################
def validarUnionConjuntos(lis,lis1):
    """
    Funcionalidad: Valida los datos de la función unionConjuntos
    Entradas:lis(lista),lis1(lista)
    Salidas: Datos validados
    """
    try:
        for i in lis:
            if not isinstance(i,int):
                print("Los valores de la lista deben ser enteros")
            elif i<0:
                print("Los elementos de la lista deben ser mayores a cero")
        for l in lis1:
            if not isinstance(i,int):
                print("Los valores de la lista deben ser enteros")
            elif i<0:
                print("Los elementos de la lista deben ser mayores a cero")
        assert lis != [] or lis1 != []
        return unionConjuntos(lis,lis1)
    
    except AssertionError:
        print("La lista de números no debe ser vacía")        
    except ValueError:
        print("Debe ingresar una lista")
    except:
        print("Llame al programador")

def mostrarUnionConjuntos():
    """
    Funcionalidad:Mostrar en pantalla la función unionConjuntos
    Salidas:Datos en pantalla
    """
    lista=[0,1,2,3,4]
    lista1=[2,3,4,5,6]
    print("A = ",lista,"\n B = ",lista1)
    print("A u B = ",validarUnionConjuntos(lista,lista1))
####RETO13##############################################################################
def validarIntercepcionConjuntos(lis,lis1):
    """
    Funcionalidad: Valida los datos de la función intercepcionConjuntos
    Entradas:lis(lista),lis1(lista)
    Salidas: Datos validados
    """
    try:
        for i in lis:
            if not isinstance(i,int):
                print("Los valores de la lista deben ser enteros")
            elif i<0:
                print("Los elementos de la lista deben ser mayores a cero")
        for l in lis1:
            if not isinstance(i,int):
                print("Los valores de la lista deben ser enteros")
            elif i<0:
                print("Los elementos de la lista deben ser mayores a cero")
        assert lis != [] or lis1 != []
        return intercepcionConjuntos(lis,lis1)
    
    except AssertionError:
        print("La lista de números no debe ser vacía")        
    except ValueError:
        print("Debe ingresar una lista")
    except:
        print("Llame al programador")

def mostrarIntercepcionConjuntos():
    """
    Funcionalidad:Mostrar en pantalla la función intercepcionConjuntos
    Salidas:Datos en pantalla
    """
    lista=[4,5,6,7,8,9]
    lista1=[0,1,6,7,9,10]
    print("A = ",lista,"\n B = ",lista1)
    print("A n B = ",validarIntercepcionConjuntos(lista,lista1))
    
####RETO14##############################################################################
def validarMultiplicarLista(lis,lis1):
    """
    Funcionalidad: Valida los datos de la función multiplicarLista
    Entradas:lis(lista),lis1(lista)
    Salidas: Datos validados
    """
    try:
        for i in lis:
            if not isinstance(i,int):
                print("Los valores de la lista deben ser enteros")
            elif i<0:
                print("Los elementos de la lista deben ser mayores a cero")
        for l in lis1:
            if not isinstance(i,int):
                print("Los valores de la lista deben ser enteros")
            elif i<0:
                print("Los elementos de la lista deben ser mayores a cero")
                
        if len(lis) != len(lis1):
            print("Las listas deben de ser del mismo tamaño")
        assert lis != [] or lis1 != []
        
        return multiplicarLista(lis,lis1)
    
    except AssertionError:
        print("La lista de números no debe ser vacía")        
    except ValueError:
        print("Debe ingresar una lista")
    except:
        print("Llame al programador")

def mostrarMultiplicarLista():
    """
    Funcionalidad:Mostrar en pantalla la función multiplicarLista
    Salidas:Datos en pantalla
    """
    lista=[5,4,3]
    lista1=[5,8,9]
    print("Lista A = ",lista,"\n Lista B = ",lista1)
    print("Por indice multiplicar A * B = ",validarMultiplicarLista(lista,lis))
    
#LlamadaFumarnesmplejado

print("Reto1 \n", mostrarSepararElementos())
print("Reto2 \n", mostrarBuscarElemento()) 
print("Reto3 \n", mostrarListaVocales())
print("Reto4 \n", mostrarLista())
print("Reto5 \n", mostrarListaAscendente())
print("Reto6 \n",mostrarEliminarElementosRepetidos())
print("Reto7 \n",mostrarSusecionUlam())
print("Reto8 \n",mostrarAlternativos())
print("Reto9 \n",mostrarListaAscendente())
print("Reto10 \n",mostrarReplicar())
print("Reto11 \n",mostrarDiferenciaConjuntos())
print("Reto12 \n",mostrarUnionConjuntos())
print("Reto13 \n",mostrarIntercepcionConjuntos())
print("Reto14 \n",mostrarMultiplicarLista())

