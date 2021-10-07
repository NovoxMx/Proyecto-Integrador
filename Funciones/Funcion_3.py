from tkinter import *

def miTelefonos():
    ventana2 = Tk()
    ventana2.geometry("1280x720")
    ventana2.title("Telefonos")

    texto= Label(ventana2,text="El marco se la come")
    texto.pack()
    texto.grid(row=1, columnspan=20, sticky=W+E)

def miCargadores():
    ventana3 = Tk()
    ventana3.geometry("1280x720")
    ventana3.title("Telefonos")

    texto= Label(ventana3,text="El marco se la come")
    texto.pack()
    texto.grid(row=1, columnspan=20, sticky=W+E)

def miPlanes():
    ventana4 = Tk()
    ventana4.geometry("1280x720")
    ventana4.title("Telefonos")

    texto= Label(ventana4,text="El marco se la come")
    texto.pack()
    texto.grid(row=1, columnspan=20, sticky=W+E)

ventana = Tk()
ventana.geometry("1280x720")
ventana.title("Precio de los productos")

buscar= Label(ventana,text="Buscar:")
buscar.pack()
buscar.grid(row=1, columnspan=20, sticky=W+E)

entrada= Entry(ventana)
entrada.grid(row=2, columnspan=6, sticky=W+E)

Boton1= Button(ventana, text=" Telefono ", command= miTelefonos).grid(row=3, column=0, sticky=W+E, columnspan=20)
Boton2= Button(ventana, text="Cargadores", command= miCargadores).grid(row=4, column=0, sticky=W+E, columnspan=20)
Boton3= Button(ventana, text="  Planes  ", command= miPlanes).grid(row=5, column=0, sticky=W+E, columnspan=20)


ventana.mainloop() 