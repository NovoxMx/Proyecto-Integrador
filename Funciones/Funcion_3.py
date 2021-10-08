from tkinter import *
import tkinter

def miTelefonos():
    def miSamsung():
        ventanaTelefono.destroy()
        ventana2 = Tk()
        ventana2.geometry("720x480")
        ventana2.title("Samsung")

        texto= Label(ventana2,text="Celulares Samsung:")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.10)

        texto= Label(ventana2,text="Galaxy Note 20 Ultra --- $22,499.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.20)
        

        texto= Label(ventana2,text="Galaxy Z Fold3 5G --- $44,999.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.30)
        

        texto= Label(ventana2,text="Samsung Galaxy A32 --- $5,499.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.40)

    def miiPhone():
        ventanaTelefono.destroy()
        ventana2 = Tk()
        ventana2.geometry("720x480")
        ventana2.title("iPhone")

        texto= Label(ventana2,text="Celulares iPhone:")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.10)
        

        texto= Label(ventana2,text="iPhone 12 --- $19,499.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.20)
        

        texto= Label(ventana2,text="iPhone 11 Pro Max --- $24,598.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.30)
        

        texto= Label(ventana2,text="iPhone X --- $8,724.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.40)

    def miHuawei():
        ventanaTelefono.destroy()
        ventana2 = Tk()
        ventana2.geometry("720x480")
        ventana2.title("Huawei")

        texto= Label(ventana2,text="Celulares Huawei:")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.10)
        

        texto= Label(ventana2,text="Huawei P40 Pro --- $14,999.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.20)
        

        texto= Label(ventana2,text="Huawei Mate 40 PRO --- $25,999.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.30)
        

        texto= Label(ventana2,text="Huawei P30 lite --- $5,639.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.40)

    def miXiaomi():
        ventanaTelefono.destroy()
        ventana2 = Tk()
        ventana2.geometry("720x480")
        ventana2.title("Xiaomi")

        texto= Label(ventana2,text="Celulares Xiaomi:")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.10)
        

        texto= Label(ventana2,text="Xiaomi Redmi Note 10 Pro --- $8,399.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.20)
        

        texto= Label(ventana2,text="Xiaomi Mi Mix 2S --- $9,999.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.30)
        

        texto= Label(ventana2,text="Xiaomi Mi 11 lite --- $6,999.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.40)

    def miMotorola():
        ventanaTelefono.destroy()
        ventana2 = Tk()
        ventana2.geometry("720x480")
        ventana2.title("Motorola")

        texto= Label(ventana2,text="Celulares Motorola:")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.10)
        

        texto= Label(ventana2,text="Motorola Moto G60 --- $7,299.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.20)
        

        texto= Label(ventana2,text="Motorola Edge 20 --- $10,999.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.30)
        

        texto= Label(ventana2,text="Motorola XT2125-4 --- $13,199.00")
        texto.config(fg="black", bg="white")
        texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.40)
        
    ventana.destroy()
    ventanaTelefono = Tk()
    ventanaTelefono.geometry("720x480")
    ventanaTelefono.title("Telefonos")

    texto= Label(ventanaTelefono,text="Seleccione la Marca que quiere ver:")
    texto.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.10)

    Boton1_1= Button(ventanaTelefono, text="Samsung", command= miSamsung).place(relwidth=0.5,relheight=0.10,relx=.25,rely=.20)
    Boton1_2= Button(ventanaTelefono, text="iPhone", command= miiPhone).place(relwidth=0.5,relheight=0.10,relx=.25,rely=.30)
    Boton1_3= Button(ventanaTelefono, text="Huawei", command= miHuawei).place(relwidth=0.5,relheight=0.10,relx=.25,rely=.40)
    Boton1_3= Button(ventanaTelefono, text="Xiaomi", command= miXiaomi).place(relwidth=0.5,relheight=0.10,relx=.25,rely=.50)
    Boton1_3= Button(ventanaTelefono, text="Motorola", command= miMotorola).place(relwidth=0.5,relheight=0.10,relx=.25,rely=.60)

def miCargadores():

    ventana.destroy()
    ventana3 = Tk()
    ventana3.geometry("720x480")
    ventana3.title("Cargadores")

    texto= Label(ventana3,text="El marco se la come")
    texto.pack()
    texto.config(fg="white", bg="black")
    texto.grid(row=1, columnspan=20, sticky=W+E)



ventana = Tk()
ventana.geometry("720x480")
ventana.title("Precio de los productos")

buscar= Label(ventana,text="Buscar:")
buscar.config(fg="black", bg="white")
buscar.place(relwidth=0.5,relheight=0.10,relx=.25,rely=.20)

Boton1= Button(ventana, text=" Telefono ", command= miTelefonos).place(relwidth=0.5,relheight=0.10,relx=.25,rely=.30)
Boton2= Button(ventana, text="Cargadores", command= miCargadores).place(relwidth=0.5,relheight=0.10,relx=.25,rely=.40)

ventana.mainloop() 