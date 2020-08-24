#Elaborado por Mario Lara Molina
#Fecha de creacion: 12/03/2020 21:14
#Ultima modificacion: 12/03/2020 21:53
#Version: 3.8.1

#Librerias
from miLibreria import *

#algoritmo que muestra uno a uno los valores que componen una cifra numerica

#Definicion de funciones
def mostrarElementoVali(pedirDatos):
    """
    funcionalidad:validar si me ingresan numeros enteros
    entradas: pcifra(numero que me ingresan)
    salidas: ver si es entero o no
    """
    if (isinstance(pedirDatos,int)== True):
        return mostrarElemento(pedirDatos)
    elif pedirDatos<=0:
        return  "El valor debe ser mayor a cero."
    else:
        return "El dato ingresado debe ser entero"
    
def mostrar():
    """
    funcionalidad: pedir datos
    entradas: cifra(numero que el usuario ingresa)
    salidas: mostrar el resultado
    """
    
    return mostrarElementoVali(cifra)
        
#PP #esta funcion corre sin la de mostrar pero al momento de dividir los numeros me termina tirando un cero que nada que ver
    
num=int(input("Ingrese un valor"))
print (mostrarElementoVali(num))
##############################################################################
#Elaborado por Mario Lara Molina
#Fecha de creacion: 12/03/2020 22:30
#Ultima modificacion: 12/03/2020 22:54
#Version: 3.8.1

#algoritmo que descompone un numero y me imprime solo los pares
#Definicion de funciones
def mostrarParesVali(pedirDatos):
    """
    funcionalidad:validar si me ingresan numeros enteros
    entradas: pcifra(numero que me ingresan)
    salidas: ver si es entero o no
    """
    if (isinstance(pedirDatos,int)== True):
        return mostrarPares(pedirDatos)
    elif pedirDatos<=0:
        return  "El valor debe ser mayor a cero."
    else:
        return "El dato ingresado debe ser entero"

#PP
num2= int(input("Ingrese un valor"))
print (mostrarParesVali(num2))

#################################################################################
#Elaborado por Mario Lara Molina
#Fecha de creacion: 12/03/2020 23:05
#Ultima modificacion: 12/03/2020 00:12
#Version: 3.8.1

#algoritmo que me dice si una cifra tiene al menos un cero o ninguno 
                  
def encontrarAlmenosUnCeroAux(cifNum):
    if(isinstance (cifNum,int)==True):
       return encontrarAlmenosUnCero(cifNum)
    elif encontrarAlmenosUnCero(cifNum)<=0:
        return  "El valor debe ser mayor a cero."
    else:
        return "El dato ingresado debe ser entero"
  
#PP 
num3=int(input('Digite el valor a revisar: '))
print(encontrarAlmenosUnCero(num3))

########de aqui en adelante no me dio tiempo a hacerlos yo solo y esto es lo que pude rescartar de la clase donde revisamos estos ejercicios(Tengo que ponerle mas)

def espar(pnum):
    if pnum%2==0:
        return True
    else:
        return False
def multiplicarImpares(pnum):
    """
    Funcionalidad: Me separa valores de una cifra y multiplica los numeros impares denro de la misma)
    Entradas: pNum(numero que ingresa el usuario)
    Salidas: Resultado de la multiplicacion de los numero impares
    """
    multiplicacion=1
    while pnum!=0:
        if espar(pnum)==False:
            multiplicacion=multiplicacion*(pnum%10)
        pnum= pnum//10
    return multiplicacion
#PP
num=int(input("Digite un numero: "))
print ("La multiplicacion de las cifras impares es: ",multiplicarImpares(num))

###########################################################################################
def buscarRepeticiones(pnum,pcont):
    """
    Funcionalidad: Contar cuantas veces aparece un digito en una cifra numerica
    Entradas: pnum(numero ingresado por el usuario), pcont(numero a buscar en la cifra)
    Salidas: Cantidad de veces que aparece el numero
    """
    apar=0
    while pnum!=0:
        if pnum%10==pcont:
            apar+=1
        pnum=pnum//10
    return(apar)

#PP
num=int(input("Digite una cifra numerica: "))
cont=int(input("Digite el numero a buscar la cantidad de apariciones en la cifra: "))
print("Apariciones=",buscarRepeticiones(num,cont))
        
########################################################################            
def determinarMayor(pnum):
    numMay=0
    while pnum!=0:
        numEvaluado=pnum%10
        if numEvaluado>numMay:
            numMay=numEvaluado 
        pnum=pnum//10
    return ("El digito mayor es: "+str(numMay))
def determinarMayorAux(pnum):
    if(isinstance(pnum,int)==False):
        return "El valor debe ser unicamente entero"
    elif(isinstance(pnum,str)==True):
        return "Debe ingresar un dato numerico"
    else:
        return determinarMayor(pnum)
#PP
num=int(input("Ingrese una cifra numerica: "))
print(determinarMayorAux(num))

##########################################################################
def elevarNumero(pBase,pExponente):
    """
    Funcion:Elevar un numero
    Entradas: Base y exponente(ambos ingresados por el usuario)
    Salida: Resultado de la elevancion exponencial
    """
    resultado=1
    while pExponente!=0:
        resultado= pBase*resultado
        pExponente-=1
    return resultado

def validar(pBase,pExponente):
    """
    Funcionalidad: Validar datos de elevarNumero(pBase,pExponente)
    Entradas: Base y exponente
    Salidas: Anuncio o ir a elevarNumero
    """
    if (pBase>=0)and(pExponente>=0)==True:
        return "El resultado de la potencia es: "+ str(elevarNumero(pBase,pExponente))
    else:
        return "Los datos deben ser enteros mayores o iguales que cero"

#PP
base=int(input("ingrese la base de la potencia: "))
exponente=int(input("ingrese el exponente de la potencia: "))
print (validar(base,exponente))

###########################################################################
def esNumeroPrimo(num):
    """
    Funcionalidad:Saber si el numero ingresado es primo o no
    Entradas:int(numero)
    Salidas: si es primo o no
    """
    contador=1
    numeroPrimo=0
    while(contador<=num):
        if(num%contador==0):
            numeroPrimo+=1
        contador+=1
    return numeroPrimo

def esNumeroPrimoAux(num):
    if isinstance (num,int)==False:
        return "El valor debe ser un numero entero"
    elif num==1 or num==0:
        return "El valor no es primo pues solo tiene un divisor"
    else:
        if esNumeroPrimo(num)==2:
            print ("Es primo")

        else:
            print("No es primo")
    return
#PP
numero=int(input("Ingrese un numero entero"))
print(esNumeroPrimoAux(numero))

############################################################################
def sumarDigitosMultiplos(pnum,pdig):
    """
    Funcion:Sumar los digitos que son multiplos de pdigit
    Entradas: pnum(int)(numero ingresado por el usuario), pdigit(int)(numero que\
    se estimara si un digito del primer numero se suma o no)
    Salidas:(int)Multiplicacion de los numeros impares
    """
    
    if isinstance(pnum,int) and isinstance(pdig,int)and pnum>0 and pdig>0:
        suma=0
        while pnum!=0:
            compr=pnum%10
            if compr%pdig==0:
                suma+=compr
            pnum=pnum//10
        return(suma)
    else:
        return"Dato de entrada no valido"
#PP
num=int(input('Ingrese un numero'))
dig=int(input('Ingrese un digito'))
print ("el resultado de la suma de digitos multiplos es:"+str(sumarDigitosMultiplos(num,dig)))
    
            
            
   
################################################################################
def esBinario(pnum):
    """
    Funcion: Decir si los digitos de una cifra son binarios o no
    Entradas: pnum(int)(numero ingresado por el usuario)
    Salidas: (str)" tiene al menos un cero o no tiene ceros"
    """
    if type(pnum)==int and pnum>0:
        while pnum!=0:
            if pnum%10 !=0 and pnum%10!=0:
                return (False)
            pnum=pnum//10
        return (True)
    else:
        return(0)

#PP
num=int(input("Digite una cifra numerica: "))
print (esBinario(num))
        
            
            
        


    
    
        
  
    





    
