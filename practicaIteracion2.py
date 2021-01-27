#Creado por Mario Lara Molina y Leonardo Fariña
#Creación: 14/03/2020 14:52 
#Modificación: 14/03/2020 16:42 
#Versión: 3.8.1

#Algoritmo que dados tres numeros los invierte de lugar

#Importación de librerias

#Definición de funciones

def formarNumeroInverso (numP1,numP2,numP3):
    '''
    Funcionalidad: Invertir los digitos ingresados por el usuario
    Entradas: numP1,numP2,numP3(numero de un solo digito ingresado por el usuario)
    Salidas: El numero invertido
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
            if 9>=numP1>=0 and 9>=numP2>=0 and 9>=numP3>=0:
                return print(formarNumeroInverso(numP1,numP2,numP3))
                break
            else:
                print("Los datos deben ser numeros entre menor o igual a 9 y mayor o igual a 0 ")
                break
            
        except ValueError:
            return ("Los datos deben ser numeros")

        except:
            return ("Tenemos un problema,no encontramos al mago")    

        
#Programa Principal

num0=(int(input("Escriba el número para ver la magia: ")))
num1=(int(input("Escriba el siguiente numero para ver la magia: ")))
num2=(int(input("Escriba el último numero para ver la magia: ")))
print(formarNumInvValid(num0,num1,num2))

#############################################################################################################################################################
 
#Elaborado por Mario Lara Molina y Leonardo Fariña
#Fecha de creacion:14/03/2020 
#Ultima modificacion: 14/03/2020 
#Version:3.8.1

        

     

        
        
