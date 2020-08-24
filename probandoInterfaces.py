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
raiz.resizable(1,True) #El primer parametro es el ancho y el segundo el alto, deben ser booleanos
raiz.iconbitmap("fantasma.ico")#es para cambiar el icono de la ventana, debe ser .ico
raiz.config(bg="LightBlue")#Para cambiar el fondo de la ventana, el color debe ser en ingles
#raiz.geometry("800x800") #Para cambiar el tamanno predeterminado de la ventana,el primero es ancho y el segundo largo
#si le pongo tamaño a la raiz  el  frame no puede aparecer
#Creacion de lo que va dentro de la ventana
mensaje= Label(raiz,bg="LightGreen",text="Hola mi neiro")#puedo no tenerlo en variable si no la voy a volver a usar
mensaje.pack(anchor="nw")#Esto es para que sea visible en pantalla y el anchor es para posicionarlo en la pantalla

#Creacion del Frame
cajaframe=Frame(raiz)#Para crear el frame
cajaframe.pack()#Para que sea visible en pantalla
cajaframe.config(bg="Orange")#Para cambiarle el color
cajaframe.config(width="400", height="200")#Para darle tamaño, primero ancho y luego alto
cajaframe.pack(expand=1, anchor='se')#Para ubicarlo, si pongo 1 se va al centro centro y si pongo 0 se va al centro arriba
#Creacion de botones
buton1= Button(raiz,text="Neiro",relief="raise")#con esto creo el boton, le pongo texto y cambio su relieve
buton1.config(bg="Blue")#Para cambiarle el color de fondo al boton
buton1.config(activeforeground="Yellow")#Cambia el color de las letras cuando presiono el boton
buton1.config(activebackground="Black")#Cambia el color del fondo del boton cuando presiono el boton
buton1.config(bd=40)#Le agrega un borde al boton
buton1.config(fg="black")#Cambia el color de las letras del boton antes de que se presione
buton1.config(font=("papyrus",32))#Cambia el tipo de letra y el tamanno

buton1.pack(anchor="center",expand=1)#Esto es para que sea visibe en pantalla
 
#Obtener Datos
#cget(), sirve para obtener un string dado por el usuario #no lo logro
#mensaje=Label(self.parent,text="Hola mi neiro")
#mensaje.cget('background')#Para obtener el fondo
#mensaje.cget('relief')#Para obtener el borde
#mensaje.cget('text')#Para obtener el texto

#configure, devuelve las opciones y configuraciones disponibles
mensaje.configure("background")
mensaje.configure() #Me tira todas las opciones
raiz.mainloop() #Siempre de ultimo lugar


