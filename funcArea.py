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

#Programa principal
base=int(input("Indique el valor de la base: "))
altura=int(input("Indique el valor de la altura: "))
print("El resultado del área es: "+str(calcularArea(base, altura)))
