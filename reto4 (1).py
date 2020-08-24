#Creado por Leonardo Fariña y Mario Lara
#Creación: 15/03/2020 11:50am
#Modificación: 15/03/2020 13:10pm
#Versión: 3.8.2

#Importación de librerias



#Definición de funciones

def obtenerCantidades (numP1):
    '''
    Funcionalidad: Devolver la cantidad de numeros pares e impares
    Entradas: numP1 validado por obtenerCantValid
    Salidas: digPar y DigImpar 
    '''
    digPar = obtenerPares(numP1)
    digImp = 0
    miDigit=0
    numSalI=0
    numSalP=0
    numSalTot=0
    if digPar!= 0:
        digPar =len(str(obtenerPares(numP1)))
    while numP1!=0:
        miDigit= numP1%10
        if (miDigit%2)==1:
            numSalI= (str(miDigit)+str(numSalI))
            digImp+=1
        numP1 = numP1 // 10
    return digPar,digImp

def obtenerPares (numP1):
    '''
    Funcionalidad: Devolver un numero con todos los digitos pares en orden ej:(Ent:1234->Sal:24) 
    Entradas: numP1 validado por obtenerParValid
    Salidas: numSalidaTot es el numero de todos los digitos pares de numP1 en orden ej:(Ent:1234->Sal:24)
    '''
    miDigit=0
    numSal=0
    numSalTot=0
    while numP1!=0:
        miDigit= numP1%10
        if (miDigit%2)==0:
            numSal= (str(miDigit)+str(numSal))
        numP1 = numP1 // 10
    numSalidaTot= int(numSal)//10
    return numSalidaTot

def obtenerCantValid (numP1):
    '''
    Funcionalidad: Determinar si la entrada cumplen los requisitos para la funcion
    Entradas: numP1 entradas de numeros,letras,etc.
    Salidas: La salida es un print((N°Pares,N°Impares)obtenerCantidades(numP1))
    '''
    while True:  
        try:
            numP1=int(numP1)
            if numP1>0:
                return print('(N°Pares,N°Impares)',obtenerCantidades(numP1))
            else:
                return print('El dato para la magia debe ser un numero mayor a 0')
        except ValueError:
            return print('El dato para la magia debe ser un numero entero')
        except:
            return print('Tenemos un problema,no encontramos al mago')
    
#Programa Principal

num0=(input("Escriba el número para ver la magia: "))
obtenerCantValid(num0)
 
