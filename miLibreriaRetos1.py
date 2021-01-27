#Creado por Leonardo Fariña y Mario Lara
#Creación: 15/03/2020 15:55 pm
#Modificación: 15/03/2020 17:23pm
#Versión: 3.8.2

#Importación de librerias

###Esta es la libreria miLibreriaRetos1
###Estas son sus funciones
'''
help(formarNumeroInverso)
help(formarNumInvValid)
help(obtenerPares)
help(obtenerParValid)
help(obtenerFactorial)
help(obtenerFacValid)
help(obtenerCantidades)
help(obtenerCantValid)
help(obtenerSumatoria)
help(obtenerSumValid)
help(convertirABinario)
help(convertirABinValid)
help(invertirNumero)
help(invertirNumValid)
'''


#Definición de funciones

def formarNumeroInverso (numP1,numP2,numP3):
    '''
    Funcionalidad: Invertir los digitos de entrada
    Entradas: numP1,numP2,numP3 de numeros validados por la funcion formarNumInvValid
    Salidas: numSalidaTot es el numero inverso de ("numP1"+"numP2"+"numP3")
    '''
    numTot=0
    miDigit=0
    numSal=0
    numSalTot=0
    cont=3
    numTot= (numP3*1)+(numP2*10)+(numP1*100)
    while cont!=0:
        if numTot!= 0:
            miDigit= numTot%10
            numSal= (str(numSal)+ str(miDigit))
            numTot = numTot // 10
        cont-=1
    numSalidaTot= int(numSal)*1
    return numSalidaTot

def formarNumInvValid (numP1,numP2,numP3):
    '''
    Funcionalidad: Determinar si las entradas cumplen los requisitos para la funcion
    Entradas: numP1,numP2,numP3 entradas de numeros,letras,etc.
    Salidas: numP1,numP2,numP3 salidas de numeros que cumplen el requisito de estar entre menor o igual a 9 y mayor o igual a 0
    '''
    while True:  
        try:
            numP1=int(numP1)
            numP2=int(numP2)
            numP3=int(numP3)
            if 9>=numP1>=0 and 9>=numP2>=0 and 9>=numP3>=0:
                return formarNumeroInverso(numP1,numP2,numP3)    
            else:
                return 'Los datos para la magia deben ser numeros entre menor o igual a 9 y mayor o igual a 0 '                
        except ValueError:
            return 'Los datos para la magia deben ser numeros'
        except:
            return 'Tenemos un problema,no encontramos al mago'
        
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

def obtenerParValid (numP1):
    '''
    Funcionalidad: Determinar si la entrada cumplen los requisitos para la funcion
    Entradas: numP1 entradas de numeros,letras,etc.
    Salidas: numP1 salida de numero que cumplen el requisito de ser un número mayor a 0
    '''
    while True:  
        try:
            numP1=int(numP1)
            if numP1>0:
                return obtenerPares(numP1)
            else:
                return 'El dato para la magia debe ser un numero mayor a 0'
        except ValueError:
            return 'El dato para la magia debe ser un numero entero'
        except:
            return 'Tenemos un problema,no encontramos al mago'
        
def obtenerFactorial (numP1):
    '''
    Funcionalidad: Devolver el factorial del numero de entrada 
    Entradas: numP1 validado por obtenerFactorialValid
    Salidas: numSalidaTot es el factorial del numero de entrada numP1
    '''
    numSal=1
    cont=1
    while cont <= numP1:
        if cont <= numP1:
            numSal=numSal*cont
            cont+=1
    return numSal

def obtenerFacValid (numP1):
    '''
    Funcionalidad: Determinar si la entrada cumplen los requisitos para la funcion
    Entradas: numP1 entradas de numeros,letras,etc.
    Salidas: numP1 salida de un numero que cumplen el requisito de ser un número entero natural
    '''
    while True:  
        try:
            numP1=int(numP1)
            if numP1>0:
                return obtenerFactorial(numP1)
            else:
                return 'El dato para la magia debe ser un numero mayor a 0'
        except ValueError:
            return 'El dato para la magia debe ser un numero entero'
        except:
            return 'Tenemos un problema,no encontramos al mago'

def obtenerCantidades (numP1):
    '''
    Funcionalidad: Devolver la cantidad de numeros pares e impares
    Entradas: numP1 validado por obtenerCantValid
    Salidas: digPar y digImp (cantidad de digitos pares,impares)
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
                return obtenerCantidades(numP1)
            else:
                return 'El dato para la magia debe ser un numero mayor a 0'
        except ValueError:
            return 'El dato para la magia debe ser un numero entero'
        except:
            return 'Tenemos un problema,no encontramos al mago'

def obtenerSumatoria (numP1):
    '''
    Funcionalidad: Devolver la sumatoria Z de i**2 empezando desde 1 hasta numP1
    Entradas: numP1 validado por obtenerSumValid
    Salidas: numSal es la sumatoria Z de i**2 empezando desde 1 hasta numP1
    '''
    numSal=0
    cont=1
    while cont <= numP1:
        if cont <= numP1:
            numSal=(numSal)+(cont**2)
            cont+=1
    return numSal

def obtenerSumValid (numP1):
    '''
    Funcionalidad: Determinar si la entrada cumplen los requisitos para la funcion
    Entradas: numP1 entradas de numeros,letras,etc.
    Salidas: ejecucion de la funcion obtenerSumatoria(numP1) con el numero validado
    '''
    while True:  
        try:
            numP1=int(numP1)
            if numP1>0:
                return obtenerSumatoria(numP1)
            else:
                return 'El dato para la magia debe ser un numero mayor a 0'
        except ValueError:
            return 'El dato para la magia debe ser un numero entero'
        except:
            return 'Tenemos un problema,no encontramos al mago'

def convertirABinario (numP1):
    '''
    Funcionalidad: convertir el numero de entrada a binario
    Entradas: numP1 numero entero 
    Salidas: numConBin() numP1 converitdo a numero binario
    '''
    numConBin=0
    while numP1!=0:
        if numP1>0:
            digBin=numP1%2
            numConBin=str(digBin)+str(numConBin)
            numP1=numP1//2
    numConBin=int(numConBin)//10
    return  numConBin


def convertirABinValid (numP1):
    '''
    Funcionalidad: Determinar si la entrada cumplen los requisitos para la funcion
    Entradas: numP1 entradas de numeros,letras,etc.
    Salidas: numConBin(numP1)Validado
    '''
    while True:  
        try:
            numP1=int(numP1)
            if numP1>0:
                return convertirABinario(numP1)
            else:
                return 'El dato para la magia debe ser un numero mayor a 0'
        except ValueError:
            return 'El dato para la magia debe ser un numero entero'
        except:
            return 'Tenemos un problema,no encontramos al mago'

def invertirNumero (numP1):
    '''
    Funcionalidad: Invertir el numero de la entrada numP1 Ej(123)->(321)
    Entradas: numP1 validado por la funcion invertirNumValid
    Salidas: numSalidaTot es el numero invertido de numP1
    '''
    cont=len(str(numP1))
    cont2=len(str(numP1))
    numSal=0
    numSalidaTot=0
    miDigit=1
    ceroDer=0
    x=False
    ceroDerSal= ""
    while numP1!=0:
        if numP1%10==0:
            x=True
        else:
            x=False
            break
        if x==True:
            ceroDerSal= str(ceroDerSal)+ str(ceroDer)
            x=False
        numP1 = numP1 // 10
    while cont!=0:
        if numP1!= 0:    
            miDigit= numP1%10
            numSal= (str(numSal)+ str(miDigit))
            numP1 = numP1 // 10
        cont-=1
    numSalidaTot= int(numSal)*1
    numSalidaTot= str(ceroDerSal) + str(numSalidaTot)
    return numSalidaTot

def invertirNumValid (numP1):
    '''
    Funcionalidad: Determinar si la entrada cumplen los requisitos para la funcion
    Entradas: numP1 entradas de numeros,letras,etc.
    Salidas: numConBin(numP1)Validado
    '''
    while True:  
        try:
            numP1=int(numP1)
            if numP1>9:
                return invertirNumero (numP1)
            else:
                return 'El dato para la magia debe ser un numero de dos digitos positivo'
        except ValueError:
            return 'El dato para la magia debe ser un numero entero de dos digitos'
        except:
            return 'Tenemos un problema,no encontramos al mago'


#Programa Principal
 
