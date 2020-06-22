#Creado por: Gilbert Rodríguez Mejias y Raúl Sanabria Marroquín
#Fecha de creación: 15/05/2020 10:05 a.m
#Última modificacion: 18/05/2020 1:16 p.m
#Version 3.8.1

def opcionReposteria(palab):
    """
    Función para determinar si el pedido de repostería es salado o dulce.
    Entrada: Parte del codigo.
    Salida: Opción de reposteria deseada.
    """
    if palab[2]=="S":
        return "salada"
    elif palab[2]=="D":
        return "dulce"

def saborEmpanada(palab):
    """
    Función para determinar el sabor de la repostería deseada.
    Entrada: Parte del codigo
    Salida: Sabor de reposteria deseada.
    """
    sabor = ""
    if palab[4]=="1":
        return "pollo"
    elif palab[4]=="2":
        return "carne"
        

def tamannoEmpanada(palab):
    """
    Función para determinar el tamaño de la repostería.
    Entrada: Parte del codigo
    Salida: Tamaño de la reposteria deseada.
    """
    if palab[5:]=="PQ":
        return "pequeña"
    elif palab[5:]=="MD":
        return "mediana"
    elif palab[5:]=="GD":
        return "grande"
    
def tipoReposteria(palab):
    """
    Función para determinar el tipo de repostería deseado.
    Entrada: Parte del codigo.
    Salida: Tipo de repostería deseada.
    """
    reposteria=["Nidito","Palito de queso","Orejita","Bisquit","Crocante","Enchilada","Empanada"]
    return reposteria[int(palab[3])-1]

def obtenerReposteria(palab):
    """
    Función para decir todos los datos sobre el tipo de respoteria.
    Entrada: Parte del codigo.
    Salida: Tipo de repostería deseada.
    """
    if palab[3] in "1,2,3,4,5,6":
        print("Usted solicita una repostería de sabor",opcionReposteria(palab),"\
        correspondiente a un:",tipoReposteria(palab))
    elif palab[3]=="7":
        print("Usted solicita una repostería de sabor",opcionReposteria(palab),"correspondiente a una:\
        ",tipoReposteria(palab),"de ",saborEmpanada(palab),tamannoEmpanada(palab))
    return ""
           
           
def tallaQueque(palab):
    """
    Función para determinar la talla de el queque.
    Entrada: Parte del codigo
    Salida: Talla de el queque.
    """
    if palab[2:4]=="GR":
        return "grande, 12 porciones"
    elif palab[2:4]=="PQ":
        return "pequeño 4 porciones"

def saborQueque(palab):
    """
    Función para determinar el sabor del queque.
    Entrada: Parte del codigo
    Salida: Sabor de el queque deseado.
    """
    if palab[4:]=="FR":
        return "fresa-chocolate"
    elif palab[4:]=="VN":
        return "vanilla"
    elif palab[4:]=="CM":
        return "caramelo"
    elif palab[4:]=="CE":
        return "chocolte"
def obtenerQueque(palab):
    """
    Función para determinar el queque.
    Entrada: Parte del codigo
    Salida: totdo el tipo de queque que pidio.
    """
    print("Usted solicita un queque de sabor ",saborQueque(palab),", de tamaño:",tallaQueque(palab))
    return ""

def tortaChilena(palab):
    """
    Función para enseñar el resultado de la torta chilena.
    Entrada: Parte del codigo
    Salida: Resultado de la torta chilena.
    """
    print("Usted solicita una torta chilena, de tamaño:grande.")
    return ""

        
        
        
        

        
