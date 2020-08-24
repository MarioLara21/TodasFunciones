#Elaborado por: Laura Coto Sarmiento
#Fecha de creación: X de X del 20XX, 7:30am 
#Ultima modificación: X de X del 20XX, 8:30am 
#Versión: X.Y.Z

#Definición de funciones
def calcularArea(pbase, paltura):
        """
        Funcionalidad:Calcular el área del triángulo
        Entradas:
        -base(int): medida de la base del triángulo,
        -altura(int): medida de la altura del triángulo
        Salidas:
        -area(float):Superficie del triángulo 
        """
        area=(pbase*paltura)/2
        return area     

def calcularAreaAux(pbase, paltura):
        if isinstance(pbase,int) and isinstance(paltura,int):
                if (pbase!=0)and(paltura!=0):
                        return "El resultado del área es: "+str(calcularArea(pbase, paltura))
                else:
                        return "Los valores de base y altura deben ser mayores a cero."
        else:
                return "Los datos de entrada deben ser únicamente enteros."

def mostrarAlUsuario():
        base=int(input("Indique el valor de la base: "))
        altura=int(input("Indique el valor de la altura: "))
        print(calcularAreaAux(base, altura))
        return ""        

#Programa principal
print(mostrarAlUsuario())
