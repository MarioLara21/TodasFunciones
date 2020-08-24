#Elaborado por Mario Lara Molina
#Fecha de creacion:11/03/2020 22:05
#Ultima modificacion: 11/03/2020 22:20
#Version:3.8.1

#Algoritmo que calcula el area de un triangulo rectangulo pero con funciones
#definicion de la funcion
def calcularArea(base,altura):
    #Funcion: calcular el area de un triangulo rectangulo con la base y altura
    #Entradas: Base, altura= valores individuales que el usuario ingresa para que el programa calcule el area
    #Salidas: area= proceso de multiplicar la base y altura y luego dividirlas entre 2
    area=(base*altura)/2
    return area
#Programa principal
base= int(input("Ingrese el valor de la base: "))
altura= int(input("Ingrese el valor de la altura: "))
# aqui llamo a la funcion
print("El area del triangulo es:"+ str(calcularArea(base,altura)))

