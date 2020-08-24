#Creado por Mario Lara Molina
#Fecha de cracion:24/03/2020 10:20
#Ultima modificacion 24/03/2020
#Version 3.8.2
#Def Funciones
#importacion de librerias
try:
    from tkinter import *
except:
    raise ImportError("Se requiere el modulo tkinter")
#Creacion de la ventana de interfaz
raiz=Tk()
raiz.title("Ventana de neiros")
raiz.resizable(0,False) #El primer parametro es el ancho y el segundo el alto, deben ser booleanos
raiz.iconbitmap("fantasma.ico")#es para cambiar el icono de la ventana, debe ser .ico
raiz.config(bg="LightBlue")#Para cambiar el fondo de la ventana, el color debe ser en ingles
raiz.geometry("400x200") #Para cambiar el tamanno predeterminado de la ventana,el primero es ancho y el segundo largo
#Creacion de lo que va dentro de la ventana

raiz.mainloop() #Siempre de ultimo lugar

