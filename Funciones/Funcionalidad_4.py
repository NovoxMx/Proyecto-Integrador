# Función 4 - Registro de ventas
# Función trabajada por: Marco Montoya - A01254155 y André Castillo - A01254180

from datetime import date
from datetime import datetime
import os
clear = lambda: os.system('cls')

def quitar_producto(producto, cantidad):
    almacen_viejo = open("almacenaje.txt", "r")
    lista_almacen = almacen_viejo.readlines()
    num_actualizado = [str(int(lista_almacen[producto * 2]) - cantidad) + "\n"]
    nueva_lista = lista_almacen[:(producto * 2)] + num_actualizado \
        + lista_almacen[(producto * 2) + 1:]
    almacen_viejo.close()
    almacen_nuevo = open("almacenaje.txt", "w")
    for renglon in nueva_lista:
        almacen_nuevo.write(renglon)
    almacen_nuevo.close()


def asignar_venta_empleados(empleado, venta):
    ventas_viejas = open("ventas_empleados.txt", "r")
    lista_ventas = ventas_viejas.readlines()
    num_actualizado = [str(int(lista_ventas[empleado * 2]) + venta) + "\n"]
    nueva_lista = lista_ventas[:(empleado * 2)] + num_actualizado \
        + lista_ventas[(empleado * 2) + 1:]
    ventas_viejas.close()
    ventas_nuevas = open("ventas_empleados.txt", "w")
    for renglon in nueva_lista:
        ventas_nuevas.write(renglon)
    ventas_nuevas.close()


hora = datetime.now()
registro = []
rule = 1
print('---Bienvenido al registro, ingrese lo que se le pide.---')
print('\nEmpleado: 1-Jose, 2-Pepesio, 3-Pablo')
a_1 = int(input('Ingrese su numero de empleado: '))
emp = str(0)
while a_1 < 1 or a_1 >3:
    a_1 = int(input('Ingrese un número válido: '))
if a_1 == 1:
    emp = 'Jose'
elif a_1 == 2:
    emp= 'Pepesio'
else:
    emp = 'Pablo'


print("\nIngese el producto vendido")
print("1-Samsung, 2-Iphone, 3-Huawei, 4-Xiaomi, 5-motorola, 6-Cargadores, 7-Audifonos y protección, 8-Otros")
marca_R = int(input("Ingresa el numero de la marca: "))
while marca_R < 1 or marca_R > 8:
    marca_R = int(input('Ingrese un número válido: '))
producto = str(0)   
if marca_R == 1:
    print("\n1-Galaxy Note 20 Ultra, 2-Galaxy Z Fold3 5G, 3-Samsung Galaxy A3")
    phone_R = int(input("Ingresa el numero del telefono: "))
    while phone_R >3 or phone_R < 1:
        phone_R= int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Galaxy Note 20 Ultra'
        precio = int(22499.00)
    elif phone_R == 2:
        producto = 'Galaxy Z Fold3 5G'
        precio = int(44999.00)
    else:
        producto = 'Samsung Galaxy A3'
        precio = int(5499.00)

elif marca_R == 2:
    print("\n1-iPhone 12, 2-iPhone 11 Pro Max, 3-iPhone Xr")
    phone_R = int(input("Ingresa el numero del telefono: "))
    while phone_R >3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'iPhone 12'
        precio = int(19499.00)
    elif phone_R == 2:
        producto = 'iPhone 11 Pro Max'
        precio = int(24598.00)
    else:
        producto = 'iPhone Xr'
        precio = int(8724.00)

        
elif marca_R == 3:
    print("\n1-Huawei P40 Pro, 2-Huawei Mate 40 PRO, 3-Huawei P30 lite")
    phone_R = int(input("Ingresa el numero del telefono: "))
    while phone_R >3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Huawei P40 Pro'
        precio = int(14999.00)
    elif phone_R == 2:
        producto = 'Huawei Mate 40 PRO'
        precio = int(25999.00)
    else: 
        producto = 'Huawei P30 lite'
        precio = int(5639.00)
        
elif marca_R == 4:
    print("\n1-Xiaomi Redmi Note 10 Pro, 2-Xiaomi Mi Mix 2S, 3-Xiaomi Mi 11 lite")
    phone_R = int(input("Ingresa el numero del telefono: "))
    while phone_R >3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Xiaomi Redmi Note 10 Pro'
        precio = int(8399.00)
    elif phone_R == 2:
        producto = 'Xiaomi Mi Mix 2S'
        precio = int(9999.00)
    else:
        producto = 'Xiaomi Mi 11 lite'
        precio = int(6999.00)

        
elif marca_R == 5:
    print("\n1-Motorola Moto G60, 2-Motorola Edge 20, 3-Motorola XT2125-4")
    phone_R = int(input("Ingresa el numero del telefono: "))
    while phone_R >3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Motorola Moto G60'
        precio = int(7299.00)
    elif phone_R == 2:
        producto = 'Motorola Edge 20'
        precio = int(10999.00)
    else:
        producto = 'Motorola XT2125-4'
        precio = int(13199.00)

elif marca_R == 6:
    print("\n1-Cargador Tipo C, 2-Cargador iPhone, 3-Cargador Micro USB") 
    phone_R = int(input("Ingresa el tipo de cargador: "))
    while phone_R > 3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Cargador tipo C'
        precio = int(300.00)
    elif phone_R ==2:
        producto = 'Cargador iPhone'
        precio = int(350.00)
    else:
        producto = 'Cargador Micro USB'
        precio = int(200.00)

elif marca_R == 7:
    print("\n1-Audifonos Bluetooth, 2-Airpods, 3-Fundas, 4-Protector de pantalla")
    phone_R = int(input("Ingrese el articulo que se vendió: "))
    while phone_R > 4 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Audifonos Bluetooth'
        precio = int(500.00)
    elif phone_R ==2:
        producto = 'Airpods'
        precio = int(3899.00)
    elif phone_R ==3:
        producto = 'Fundas'
        precio = int(500.00)
    else:
        producto = 'Protector de pantalla'
        precio = int(275.00)

else:
    print('\n1-Tarjeta de memoria (64Gb), 2-Batería portatil, 3- Popsockets')
    phone_R = int(input("Ingrese el articulo que se vendió: "))
    while phone_R > 3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Tarjeta de memoria (64Gb)'
        precio = int(495.00)
    elif phone_R ==2:
        producto = 'Batería portatil'
        precio = int(1000.00)
    else:
        producto = 'Popsockets'
        precio = int(350.00)

cantidad = int(input('\nIntroduzca la cantidad de productos vendidos: '))
while cantidad < 1:
    cantidad = int(input('Introduzca una cantidad válida: '))

if marca_R == 1:   #Definir p para quitar producto
    p = phone_R
elif marca_R == 2:
    p = ((marca_R - 1) * 3) + phone_R
elif marca_R == 3:
    p = ((marca_R - 1) * 3) + phone_R
elif marca_R == 4:
    p = ((marca_R - 1) * 3) + phone_R
elif marca_R == 5:
    p = ((marca_R - 1) * 3) + phone_R
elif marca_R == 6:
    p = ((marca_R - 1) * 3) + phone_R
elif marca_R == 7:
    p = ((marca_R - 1) * 3) + phone_R
elif marca_R == 8:
    p = 22 + phone_R

quitar_producto(p, cantidad)     #Quitar productos vendidos de almacen
asignar_venta_empleados(a_1, precio)

if rule == 0:
    print('verifique que todos los valores introducidos sean válidos')
else:
    print('\nGracias por terminar su registro.')
    archivo = open('registro.txt', 'a')
    archivo.write('Empleado: ' + emp + "\n")
    archivo.write('Fecha y hora: ' + str(hora) + "\n")
    archivo.write('Producto: ' + producto + '\n')
    archivo.write('Cantidad de productos vendidos: ' + str(cantidad) + '\n\n')
    archivo.close()

print('\n•❅ ────────────✧ ❅ ✦ ❅ ✧──────────── ❅ •')
sino = int(input('\n¿Desea salir o volver al menú principal?\
                \n[1]-Salir \n[2]-Volver al menú principal\n'))
while sino < 1 or sino > 2:
    sino = int(input('Ingrese un número válido: '))
if sino == 2:
    os.system('python Programa_Principal.py')
else:
    clear()


