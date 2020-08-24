#Hecho por Leonardo Fariña
#Creación: 13/03/2020 18:39 pm
#Modificación: 13/03/2020 19:12 am
#Versión: 3.8.2

#Importación de librerias



#Definición de funciones

def formarNumeroInverso(numPru0,numPru1,numPru2):
    '''
    Funcionalidad: Darle el orden inverso de 3 número digitados
    Entradas: numPru0,numPru1,numPru2 todos enteros menores o iguales que 9 y mayores o iguales que 0
    Salidas: los digitos inversos "numPru2,numPru1,numPru0"
    '''
    testearNums(numPru0)
    testearNums(numPru1)
    testearNums(numPru2)
    if numPru0==int and numPru1==int and numPru2==int:
        numTot=0
        numAga=0
        numSalida=0
        numTot= str(numPru0) + str(numPru1) + str(numPru2)
        numTot=int(numTot)
        while numTot!= 0:
            if numTot%10>=0:
                numAga=numTot%10
                numSalida=(str(numSalida) + str(numAga))
                numTot= numTot//10
        return int(int(numSalida)*1)
    else:
        return

def testearNums(numTes):
    while True:
        try:
            if (9>=numTes>=0):
                return numTes
                break
            else:
                print("Los números tienen que ser de un solo digito y positivos")
                return
        except ValueError:
            print("Debe poner solo números")
            return
        except TypeError:
            return 
        except:
            print("Tenemos otros Inconvenientes. Procesando")
            return

        
#Programa Principal

num0=(int(input("Escriba el número para ver la magia: ")))
num1=(int(input("Escriba el siguiente numero para ver la magia: ")))
num2=(int(input("Escriba el último numero para ver la magia: ")))
print(formarNumeroInverso(num0,num1,num2))

        
    
