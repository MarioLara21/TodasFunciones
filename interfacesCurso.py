from tkinter import *
import os

def load_img(name):#Para  cargar imagenes
    path=os.path.join("imgs",name)
    img= PhotoImage(file=path)
    return img
def derecha():
    contenedor.move("BOLA",50,0)
def winB():#Para hacer ventanas secundarias
    windowB=Toplevel()
    windowB.title("VentanaB")
    windowB.minisize(300,200)
ventana= Tk()
ventana.title("Ejemplo")
ventana.minsize(800,800)#mantener estos tamaños para los proyectos
ventana.resizable(width=False, height=False)
ventana.geometry("400x400+500+150")#lo que está después del + es la posicion de la pantalla en la que va a aparecer

contenedor=Canvas(ventana, width=400, height=400,bg="Yellow")
contenedor.place(x=0,y=0)
contenedor.create_oval(1,1,160,160, width=0, fill="Green",tags="BOLA")
#crate.oval(x,y,width,heigt,....)

fIMG= load_img("descarga.png")
contenedor.crate_image(50,50,image=fIMG,tags="Aleja")
botonA= Button(ventana,width=8,height=2,command=derecha,text="Derecha")
botonA.place(x=100,y=350)


ventana.miniloop()
