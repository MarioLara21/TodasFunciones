lista=[8,7,6,5,4,3]
lista2=[1,1,1,1,1]
lista3=[8,0,6,5,0,3]
lista4=[8,5,6,5,3]
lista5=[8,2,6,8,4]
lista6=[2,3,4,5,7]
def mostrarElementoL(lista):
    print("Entrada:",lista)
    for i in lista:
        print(i)
    return
mostrarElementoL(lista)
def determinarMayorL(lista, lista2):
    mayor=0
    mayor2=0
    print("Entrada1", lista)
    for i in lista:
        if i>mayor:
            mayor=i
    print("Salida:",mayor)
    print("Entrada2",lista2)
    for o in lista2:
        if o>mayor2:
            mayor2=o
    print("Salida:",mayor2)
    return
determinarMayorL(lista,lista2)
def mostrarParesL(lista):
    print("Entrada",lista)
    for i in lista:
        if i%2==0:
            print(i)
    return
mostrarParesL(lista)
def AlmenosUnCeroL(lista3,lista4):
    print("Entrada",lista4)
    for i in lista4:
        if i==0:
            return print("True")
    return "False"
AlmenosUnCeroL(lista3,lista4)       














           
