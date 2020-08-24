palabra=input("Ingrese una palabra:")
bandera=True
contador=0
def reto():
    while contador< len(palabra):
        palabra+=len(palabra[contador])
        print(palabra)
    contador+=1

    return palabra
    
