#Creado por Leonardo Fariña y Mario Lara
#Creación: 13/03/2020 18:39 pm
#Modificación: 15/03/2020 10:50am
#Versión: 3.8.2

#Importación de librerias



#Definición de funciones

def formarNumeroInverso (numP1,numP2,numP3):
    '''
    Funcionalidad: Invertir los digitos de entrada
    Entradas: numP1,numP2,numP3 de numeros validados por la funcion formarNumInvValid
    Salidas: numSalidaTot es el numero invertido de ("numP1"+"numP2"+"numP3")
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
    
#Programa Principal

num0=(input("Escriba el número para ver la magia: "))
num1=(input("Escriba el siguiente numero para ver la magia: "))
num2=(input("Escriba el último numero para ver la magia: "))
print(formarNumInvValid(num0,num1,num2))
 
