#Creado por Mario Lara
#Fecha  de creación: 01/08/2020 16:30
#Última mocificación 01/08/2020 16:35
#Versión 3.8.1
#Importación de librerías
#Declaración de variables
univ=["A","B","C"]
#Definición de funciones
def sisPado(n,cont=0):
    """
    Funcionalidad: 
    Sistema-L de Padovan definen los siguientes enunciados:
        a.	Universo: A,B,C
        b.	P(0): A
        c.	Reglas: (A → B), (B → C), (C → AB)
        
        >>>P(0) 
        A
        >>>P(1)
        B
        >>>P(2)
        C
        >>>P(3)
        AB
        >>>P(4)
        BC
    Entradas: n= Número entero
    Salidas: Combinación del universo solicitada
    Restricciones: El parámetro ingresado debe ser únicamente entero positivo
    """
    if n==cont:
        if cont>2:
            return (univ[(cont-3)%3])+(univ[(cont-2)%3])
        else:
            return univ[cont]
    else:
        return sisPado(n,cont+1)
#PP
print("P(0)")
print(sisPado(0))
print("P(1)")
print(sisPado(1))
print("P(2)")
print(sisPado(2))
print("P(3)")
print(sisPado(3))
