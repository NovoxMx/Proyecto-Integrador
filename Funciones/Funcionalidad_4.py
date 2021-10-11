# Función 4 - Registro de ventas
# Función trabajada por - Marco Montoya A 01254155

from datetime import date
from datetime import datetime

hora = datetime.now()
registro = []
rule = 1
print('---Bienvenido al registro, ingrese lo que se le pide.---')
print('\nEmpleado: 1-Jose, 2-Pablo, 3-Pedro')
a_1 = int(input('Ingrese su numero de empleado: '))
emp = str(0)
while a_1 < 1 or a_1 >3:
    a_1 = int(input('Ingrese un número válido: '))
if a_1 == 1:
    emp = 'Jose'
elif a_1 == 2:
    emp= 'Pablo'
else:
    emp = 'Pedro'


print("\nIngese el producto vendido")
<<<<<<< HEAD:Funciones/Funcion_4.py
print("1-Samsung, 2-Iphone, 3-Huawei, 4-Xiaomi, 5-motorola, 6-Cargadores, 7-Audifonos y protección, 8-Otros")
=======
print("1-Samsung, 2-Iphone, 3-Huawei, 4-Xiaomi, 5-Motorola")
>>>>>>> 11bb2619e5106abb4eb70671a954de680795a1fe:Funciones/Funcionalidad_4.py
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
    elif phone_R == 2:
        producto = 'Galaxy Z Fold3 5G'
    else:
        producto = 'Samsung Galaxy A3'

elif marca_R == 2:
    print("\n1-iPhone 12, 2-iPhone 11 Pro Max, 3-iPhone Xr")
    phone_R = int(input("Ingresa el numero del telefono: "))
    while phone_R >3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'iPhone 12'
    elif phone_R == 2:
        producto = 'iPhone 11 Pro Max'
    else:
        producto = 'iPhone Xr'

        
elif marca_R == 3:
    print("\n1-Huawei P40 Pro, 2-Huawei Mate 40 PRO, 3-Huawei P30 lite")
    phone_R = int(input("Ingresa el numero del telefono: "))
    while phone_R >3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Huawei P40 Pro'
    elif phone_R == 2:
        producto = 'Huawei Mate 40 PRO'
    else: 
        producto = 'Huawei P30 lite'
                
        
elif marca_R == 4:
    print("\n1-Xiaomi Redmi Note 10 Pro, 2-Xiaomi Mi Mix 2S, 3-Xiaomi Mi 11 lite")
    phone_R = int(input("Ingresa el numero del telefono: "))
    while phone_R >3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Xiaomi Redmi Note 10 Pro'
    elif phone_R == 2:
        producto = 'Xiaomi Mi Mix 2S'
    else:
        producto = 'Xiaomi Mi 11 lite'

        
elif marca_R == 5:
    print("\n1-Motorola Moto G60, 2-Motorola Edge 20, 3-Motorola XT2125-4")
    phone_R = int(input("Ingresa el numero del telefono: "))
    while phone_R >3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Motorola Moto G60'
    elif phone_R == 2:
        producto = 'Motorola Edge 20'
    else:
        producto = 'Motorola XT2125-4'

elif marca_R == 6:
    print("\n1-Cargador Tipo C, 2-Cargador iPhone, 3-Cargador Micro USB") 
    phone_R = int(input("Ingresa el tipo de cargador: "))
    while phone_R > 3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Cargador tipo C'
    elif phone_R ==2:
        producto = 'Cargador iPhone'
    else:
        producto = 'Cargador Micro USB'

elif marca_R == 7:
    print("\n1-Audifonos Bluetooth, 2-Airpods, 3-Fundas, 4-Protector de pantalla")
    phone_R = int(input("Ingrese el articulo que se vendió: "))
    while phone_R > 4 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Audifonos Bluetooth'
    elif phone_R ==2:
        producto = 'Airpods'
    elif phone_R ==3:
        producto = 'Fundas'
    else:
        producto = 'Protector de pantalla'

else:
    print('\n1-Tarjeta de memoria (64Gb), 2-Batería portatil, 3- Popsockets')
    phone_R = int(input("Ingrese el articulo que se vendió: "))
    while phone_R > 3 or phone_R < 1:
        phone_R = int(input('Ingrese un número válido: '))
    if phone_R == 1:
        producto = 'Tarjeta de memoria (64Gb)'
    elif phone_R ==2:
        producto = 'Batería portatil'
    else:
        producto = 'Popsockets'
    


cantidad = int(input('\nIntroduzca la cantidad de productos vendidos: '))
while cantidad < 1:
    cantidad = int(input('Introduzca una cantidad válida: '))


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