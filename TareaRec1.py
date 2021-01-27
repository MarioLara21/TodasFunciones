#Creado por Mario Lara y Leonardo Fariña
#Fecha de creación 24/07/2020 23:27
#Última modificación 25/07/2020 15:57
#Versión 3.8.3

#Ejercicio 2
def esPar(num):
    """
    Funcionalidad: Verifica si el dígito es par
    Entradas: num= Número entero
    Salidas: Si el número es par o no
    Restricciones: El dato debe ser un número
    """
    if num%2==0:
        return True
    return False

def verificarPar(num):
    """
    Funcionalidad: Verifica si un número tiene al menos un dígito par
    Entradas: num= Número de tipo entero
    Salidas: Si el número tiene al menos un par o no
    Restricciones: El número debe ser entero
    """
    if num%10==num:
        if esPar(num)==False:
            return "La cifra numérica no posee ningún par"
    else:
        if esPar(num%10)==False:
           return verificarPar(num//10)
    return "La cifra numérica posee al menos un par"

def validarPar(num):
    """
    Funcionalidad: Valida el tipo del parámetro
    Entradas: num= Número de tipo entero
    Salidas: Dato validado y llamado a la funcion de proceso
    Restricciones: El número debe ser de tipo entero y mayor a cero
    """
    try:
        num=int(num)
        if not isinstance(num,int):
            return "El valor ingresado debe corresponder a un número entero únicamente"
        elif num<0:
            return "El número ingresado debe ser mayor a cero"
        else:
            return verificarPar(num)
        
    except:
        return "El valor ingresado debe corresponder a un número únicamente"
def pedirPar():
    """
    Funcionalidad: Pide un número 
    Entradas:NA
    Salidas: Llamada a la función de validación
    Restricciones:El dato ingresado debería ser un número entero
    """
    num=input("Ingrese un número: ")
    return validarPar(num)
#-----------------------------------------------------------------------------#

#Desafío 4
def multImpar(num):
    """
    Funcionalidad: Multiplica los números impares de una cifra
    Entradas: num= Número entero
    Salidas: Dígitos impares multiplicados
    Restricciones: El número debe ser entero
    """
    if (num//10)==0:
        if esPar(num)==False:
            return num
        else:
            return 1*num
    else:
        if esPar(num%10)==False:
            return (num%10) * multImpar(num//10)
        else:
            return multImpar(num//10)
def validarImpar(num):
    """
    Funcionalidad: Valida el número ingresado
    Entradas: num= Número entero
    Salidas: Dato validado
    Restricciones: El número debe ser entero
    """
    try:
        num=int(num)
        if not isinstance(num,int):
            return "El valor ingresado debe corresponder a un número únicamente"
        elif num<0:
            return "El número ingresado debe ser mayor a cero"
        else:
            return "La multiplicación impar es: "+str(multImpar(num))
    except:
        return "El valor ingresado debe corresponder a un número únicamente"
def pedirImpar():
    """
    Funcionalidad: Pide el número
    Entradas:NA
    Salidas:Llamada a la función
    Restricciones:NAs
    """
    num=input("Ingrese un número: ")
    return validarImpar(num)
#-----------------------------------------------------------------------------#
#Desafío 6
def determinarCant(num,dig):
    """
    Funcionalidad: Busca un dígito en una cifra ingresada
    Entradas:
    num= Número entero
    dig= Dígito a buscar
    Salidas: Cantidad de veces que aparece el dígito en la cifra ingresada
    Restricciones: El número y el dígito deben de ser tipo entero y positivos
    """
    if (num//10)==0:
        if num==dig:
            return 1
        else:
            return 0
    else:
        if (num%10)==dig:
            return 1 + determinarCant((num//10),dig)
    return determinarCant((num//10),dig)
def validarCant(num,dig):           
    """
    Funcionalidad: Valida el tipo del número y el dígito
    Entradas:
    num=Número entero
    dig= Dígito a buscar
    Salidas: Datos validados
    Restricciones: El número y el dígito deben ser enteros positivos
    """
    try:
        num=int(num)
        dig=int(dig)
        if not isinstance(num,int):
            return "El número ingresado debe ser de tipo entero"
        elif not isinstance(dig,int):
            return "El dígito ingresado debe ser de tipo entero"
        elif num<0:
            return "El número ingresado debe ser mayor a cero"
        elif dig<0:
            return "El dígito ingresado debe ser mayor a cero"
        elif dig>9:
            return "El dígito debe ser de un solo dígito"
        else:
            return determinarCant(num,dig)
    except:
        return "El número y el dígito deben ser datos de tipo entero positivos"
def pedirCant():
    """
    Funcionalidad: Pide el número y el dígito
    Entradas:NA
    Salidas:Llamada a la función
    Restricciones:NA
    """
    num=input("Ingrese un número: ")
    dig=input("Ingrese el dígito a buscar: ")
    return validarCant(num,dig)
#-----------------------------------------------------------------------------#

#Desafío 8
def esNumeroPrimo(num,cont=2):
    """
    Funcionalidad:
    Entradas:
    Salidas:
    Restricciones:
    """
    if num==0:
        return False
        


























    
