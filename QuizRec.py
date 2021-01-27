#Creado por Mario Lara Molina
#Fecha de creación 05/08/2020 7:40 am
#Última modficacion 05/08/2020
#Versión 3.8.3
#Definición de funciones
def determinarMenAux(cifra,men=9):
    if cifra==0:
        return men
    else:
        if (cifra%10)< men:
            men=(cifra%10)
        return determinarMenAux(cifra//10,men)        
def determinarMen(cifra):
    try:
        if not isinstance(cifra,int):
            return "La cifra debe de ser de tipo entero"
        elif  cifra<0:
            return "La cifra debe ser mayor  a cero"
        else:
            return determinarMenAux(cifra,men=9)
    except:
        return "Ingrese un dato de tipo entero"
