# Función 4 - Registro de ventas
# Función trabajada por - Marco Montoya A 01254155

from datetime import date
from datetime import datetime

hora = datetime.now()
registro = []
rule = 1
print('---Bienvenido al registro, ingrese lo que se le pide.---')
print('\nEmpleado: 1-Jose, 2-Pablo, 3- Pedro')
a_1 = int(input('Ingrese su numero de empleado: '))
emp = str(0)
if a_1 == 1:
    emp = 'Jose'
elif a_1 == 2:
    emp= 'Pablo'
elif a_1 == 3:
    emp = 'Pedro'
else:
    print('Introduzca un carácter valido')
    rule = 0

print("\nIngese el producto vendido")
print("1-Samsung, 2-Iphone, 3-Huawei, 4-Xiaomi, 5-motorola")
marca_R = int(input("Ingresa el numero de la marca: "))
producto = 0
if marca_R == 1:
    print("\n1-Galaxy Note 20 Ultra, 2-Galaxy Z Fold3 5G, 3-Samsung Galaxy A3")
    phone_R = int(input("Ingresa el numero del telefono: "))
    if phone_R >= 1 and phone_R <= 3:
        if phone_R == 1:
            producto = 'Galaxy Note 20 Ultra'
        elif phone_R == 2:
            producto = 'Galaxy Z Fold3 5G'
        elif phone_R == 3:
            producto = 'Samsung Galaxy A3'
        else:
            print('Introduzca un carácter valido')
            rule = 0     
    else:
        print("Introduzca un carácter valido")
        rule = 0

elif marca_R == 2:
    print("\n1-iPhone 12, 2-iPhone 11 Pro Max, 3-iPhone Xr")
    phone_R = int(input("Ingresa el numero del telefono: "))
    if phone_R >= 1 and phone_R <= 3:
        if phone_R == 1:
            producto = 'iPhone 12'
        elif phone_R == 2:
            producto = 'iPhone 11 Pro Max'
        elif phone_R == 3:
            producto = 'iPhone Xr'
        else:
            print('Introduzca un carácter valido')   
            rule = 0  
    else:
        print("Introduzca un carácter valido")
        rule = 0
    
elif marca_R == 3:
    print("\n1-Huawei P40 Pro, 2-Huawei Mate 40 PRO, 3-Huawei P30 lite")
    phone_R = int(input("Ingresa el numero del telefono: "))
    if phone_R >= 1 and phone_R <= 3:
        if phone_R == 1:
            producto = 'Huawei P40 Pro'
        elif phone_R == 2:
            producto = 'Huawei Mate 40 PRO'
        elif phone_R == 3:
            producto = 'Huawei P30 lite'
        else:
            print('Introduzca un carácter valido')
            rule = 0
            
    else:
        print("Introduzca un carácter valido")
        rule = 0
    
elif marca_R == 4:
    print("\n1-Xiaomi Redmi Note 10 Pro, 2-Xiaomi Mi Mix 2S, 3-Xiaomi Mi 11 lite")
    phone_R = int(input("Ingresa el numero del telefono: "))
    if phone_R >= 1 and phone_R<= 3:
        if phone_R == 1:
            producto = 'Xiaomi Redmi Note 10 Pro'
        elif phone_R == 2:
            producto = 'Xiaomi Mi Mix 2S'
        elif phone_R == 3:
            producto = 'Xiaomi Mi 11 lite'
        else:
            print ('Introduzca un carácter válido')
            rule = 0
    else:
        print("Introduzca un carácter valido")
        rule = 0
    
elif marca_R == 5:
    print("\n1-Motorola Moto G60, 2-Motorola Edge 20, 3-Motorola XT2125-4")
    phone_R = int(input("Ingresa el numero del telefono: "))
    if phone_R >= 1 and phone_R <= 3:
        if phone_R == 1:
            producto = 'Motorola Moto G60'
        elif phone_R == 2:
            producto = 'Motorola Edge 20'
        elif phone_R == 3:
            producto = 'Motorola XT2125-4'
        else:
            print ('Introduzca un carácter válido')
            rule = 0
    else:
        print("Introduzca un carácter válido")
        rule = 0

else:
    print("Introduzca un carácter válido")
    rule = 0

cantidad = int(input('\nIntroduzca la cantidad de productos vendidos: '))
print('')

if cantidad < 1:
    print ('Introduzca un número válido')
    rule = 0

    

    

if rule == 0:
    print('verifique que todos los valores introducidos sean válidos')
else:
    print('Gracias por terminar su registro.')
    archivo = open('registro.txt', 'a')
    archivo.write('Empleado: ' + emp + "\n")
    archivo.write('Fecha y hora: ' + str(hora) + "\n")
    archivo.write('Producto: ' + producto + '\n')
    archivo.write('Cantidad de productos vendidos: ' + str(cantidad) + '\n\n')
    archivo.close()