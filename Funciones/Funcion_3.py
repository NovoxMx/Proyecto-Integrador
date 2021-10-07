from tkinter import *

def miTelefonos():
    def miSamsung():
        ventanaTelefono.destroy()
        ventana2 = Tk()
        ventana2.geometry("1280x720")
        ventana2.title("Samsung")

        texto= Label(ventana2,text="Celulares Samsung")
        texto.pack()
        

        texto= Label(ventana2,text="Galaxy Note 20 Ultra --- $22,499.00")
        texto.pack()
        

        texto= Label(ventana2,text="Galaxy Z Fold3 5G --- $44,999.00")
        texto.pack()
        

        texto= Label(ventana2,text="Samsung Galaxy S20 FE --- $12,499.00")
        texto.pack()
        

        texto= Label(ventana2,text="Samsung Galaxy S10 --- $8,199.00")
        texto.pack()
        

        texto= Label(ventana2,text="Samsung Galaxy A32 --- $5,499.00")
        texto.pack()

    def miiPhone():
        ventanaTelefono.destroy()
        ventana2 = Tk()
        ventana2.geometry("1280x720")
        ventana2.title("iPhone")

        texto= Label(ventana2,text="Celulares iPhone")
        texto.pack()
        

        texto= Label(ventana2,text="iPhone 12 --- $19,499.00")
        texto.pack()
        

        texto= Label(ventana2,text="iPhone 11 Pro Max --- $24,598.00")
        texto.pack()
        

        texto= Label(ventana2,text="iPhone X --- $8,724.00")
        texto.pack()
        

        texto= Label(ventana2,text="iPhone 8 Plus --- $7,694.19")
        texto.pack()
        

        texto= Label(ventana2,text="iPhone Xr --- $8,724.00")
        texto.pack()

    def miHuawei():
        ventanaTelefono.destroy()
        ventana2 = Tk()
        ventana2.geometry("1280x720")
        ventana2.title("Huawei")

        texto= Label(ventana2,text="Celulares Huawei")
        texto.pack()
        

        texto= Label(ventana2,text="Huawei P40 Pro --- $14,999.00")
        texto.pack()
        

        texto= Label(ventana2,text="Huawei Mate 40 PRO --- $25,999.00")
        texto.pack()
        

        texto= Label(ventana2,text="Huawei P30 lite --- $5,639.00")
        texto.pack()
        

        texto= Label(ventana2,text="Huawei y9a --- $6,799.00")
        texto.pack()
        

        texto= Label(ventana2,text="Huawei Nova 8i --- $7,989.00")
        texto.pack()

    def miXiaomi():
        ventanaTelefono.destroy()
        ventana2 = Tk()
        ventana2.geometry("1280x720")
        ventana2.title("Xiaomi")

        texto= Label(ventana2,text="Celulares Xiaomi")
        texto.pack()
        

        texto= Label(ventana2,text="Xiaomi Poco X3 Pro --- $6,298.00")
        texto.pack()
        

        texto= Label(ventana2,text="Xiaomi Mi 11 --- $8,719.00")
        texto.pack()
        

        texto= Label(ventana2,text="Xiaomi Redmi Note 10 Pro --- $8,399.00")
        texto.pack()
        

        texto= Label(ventana2,text="Xiaomi Mi Mix 2S --- $9,999.00")
        texto.pack()
        

        texto= Label(ventana2,text="Xiaomi Mi 11 --- $6,999.00")
        texto.pack()

    def miMotorola():
        ventanaTelefono.destroy()
        ventana2 = Tk()
        ventana2.geometry("1280x720")
        ventana2.title("Motorola")

        texto= Label(ventana2,text="Celulares Motorola")
        texto.pack()
        

        texto= Label(ventana2,text="iPhone 12 --- $19,499.00")
        texto.pack()
        

        texto= Label(ventana2,text="iPhone 11 Pro Max --- $24,598.00")
        texto.pack()
        

        texto= Label(ventana2,text="iPhone X --- $8,724.00")
        texto.pack()
        

        texto= Label(ventana2,text="iPhone 8 Plus --- $7,694.19")
        texto.pack()
        

        texto= Label(ventana2,text="iPhone Xr --- $8,724.00")
        texto.pack()
        
    ventana.destroy()
    ventanaTelefono = Tk()
    ventanaTelefono.geometry("1280x720")
    ventanaTelefono.title("Telefonos")

    texto= Label(ventanaTelefono,text="Seleccione la Marca que quiere ver:")
    texto.pack()
    texto.grid(row=1, columnspan=20, sticky=W+E)

    Boton1_1= Button(ventanaTelefono, text="Samsung", command= miSamsung).grid(row=2, sticky=W+E, columnspan=20)
    Boton1_2= Button(ventanaTelefono, text="iPhone", command= miiPhone).grid(row=3, sticky=W+E, columnspan=20)
    Boton1_3= Button(ventanaTelefono, text="Huawei", command= miHuawei).grid(row=4, sticky=W+E, columnspan=20)
    Boton1_3= Button(ventanaTelefono, text="Xiaomi", command= miXiaomi).grid(row=5, sticky=W+E, columnspan=20)
    Boton1_3= Button(ventanaTelefono, text="Motorola", command= miMotorola).grid(row=6, sticky=W+E, columnspan=20)

def miCargadores():
    ventana3 = Tk()
    ventana3.geometry("1280x720")
    ventana3.title("Cargadores")

    texto= Label(ventana3,text="El marco se la come")
    texto.pack()
    texto.config(fg="white", bg="black")
    texto.grid(row=1, columnspan=20, sticky=W+E)

def miPlanes():
    ventana4 = Tk()
    ventana4.geometry("1280x720")
    ventana4.title("Planes")

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

Boton1= Button(ventana, text=" Telefono ", command= miTelefonos).grid(row=3, sticky=W+E, columnspan=20)
Boton2= Button(ventana, text="Cargadores", command= miCargadores).grid(row=4, sticky=W+E, columnspan=20)
Boton3= Button(ventana, text="  Planes  ", command= miPlanes).grid(row=5, sticky=W+E, columnspan=20)


ventana.mainloop() 