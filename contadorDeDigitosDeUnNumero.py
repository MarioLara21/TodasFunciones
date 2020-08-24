#Elaborado por Mario Lara Molina
#Fecha de creacion:11/03/2020 23:16
#Ultima modificacion: 11/03/2020 23:29
#Version:3.8.1

#Algoritmo para ver cuantos digitos tiene un numero

def mostrarDigito(pnum) : # sacar la cantidad de digitos 
    """
    funcion: para cualquie numero que yo escriba me va a decir cuantos digitos tiene
    Entradas: num= cualquier numero entero mayor que cero que el usuario ingrese
    Salidas= cantidad de digitos que tiene el numero
    """
    while pmun != 0 :
        print(pmun%10)
        pmun= pmun//10
    return" "

def mostrarDigitoAux (pnum) : #validar si los valores ingresados son numeros
        if (isinstance (pnum,int) ==False) :
                return "El dato debe ser un numero entero"
        elif pnum <=0 :
                return " El dato debe ser mayor a cero"
        else :
            return " los digitos son: "+str(mostrarDigito(pnum))
#programa principal
num= int(input('Ingrese el numero a descomponer: '))        
print (mostrarDigitoAux(num))

