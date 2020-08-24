#Elaborado por Mario Lara Molina
#Fecha de creacion: 12/03/2020 21:14
#Ultima modificacion: 12/03/2020 21:53
#Version: 3.8.1

#algoritmo que muestra uno a uno los valores que componen una cifra numerica

#Definicion de funciones
def mostrarElemento(pedirDatos ):
    """
    Funcionalidad: Devuelve un numero digito por digito
    Entradas: cifra(numero entero)
    Salidas: numero descompuesto
    """
    try:
         while  pedirDatos!= 0:
            print(pedirDatos%10)
            pedirDatos = pedirDatos//10
         return "" 
    except:
        print (mostrarElementos(pedirDatos))
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
    cifra= int(input("ingrese un valor: "))
    return mostrarElementoVali(cifra)

#PP
num=int(input("Ingrese un valor"))
print (mostrarElementoVali(num))
