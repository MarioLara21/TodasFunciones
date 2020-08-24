#Creado por Leonardo Fariña y Mario Lara
#Creación: 15/03/2020 14:15 pm
#Modificación: 15/03/2020 15:52pm
#Versión: 3.8.2

#Importación de librerias


#Definición de funciones

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

num0=(input("Escriba el número para ver la magia: "))
print(invertirNumValid(num0))
 
