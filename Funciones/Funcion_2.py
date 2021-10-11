def samsung(telefono):
    if telefono == 1:
        print('\nGalaxy Note 20 Ultra \nMemoria ram = 12 GB RAM LPDDR5 \nCapacidad de almacenamiento = 256/512 (con MicroSD\nPantalla = Dynamic AMOLED 6,9" 3.088 x 1.440 px WQHD+')
    elif telefono  == 2:
        print("\nGalaxy Z Fold3 5G \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
    else:
        print("\nSamsung Galaxy A32 \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
        

def iphone(telefono):
    if telefono == 1:
        print("\niPhone 12 \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
    elif telefono  == 2:
        print("\niPhone 11 Pro Max \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
    else:
        print("\niPhone Xr \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
        

def huawei(telefono):
    if telefono == 1:
        print("\nHuawei P40 Pro \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
    elif telefono  == 2:
        print("\nHuawei Mate 40 PRO \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
    else:
        print("\nHuawei P30 lite \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
        

def xiaomi(telefono):
    if telefono == 1:
        print("\nXiaomi Redmi Note 10 Pro \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
    elif telefono  == 2:
        print("\nXiaomi Mi Mix 2S \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
    else:
        print("\nXiaomi Mi 11 lite \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
        

def motorola(telefono):
    if telefono == 1:
        print("\nMotorola Moto G60 \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
    elif telefono  == 2:
        print("\nMotorola Edge 20 \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
    else:
        print("\nMotorola XT2125-4 \nMemoria ram = \nCapacidad de almacenamiento = \nPantalla = ")
        

    
print("1-Samsung, 2-Iphone, 3-Huawei, 4-Xiaomi, 5-motorola")
marca = int(input("Ingresa el numero de la marca: "))

if marca == 1:
    print("\n1-Galaxy Note 20 Ultra, 2-Galaxy Z Fold3 5G, 3-Samsung Galaxy A3")
    phone = int(input("Ingresa el numero del telefono: "))
    if phone >= 1 and phone <= 3:
        samsung(phone)
    else:
        print("Numero invalido")
        
elif marca == 2:
    print("\n1-iPhone 12, 2-iPhone 11 Pro Max, 3-iPhone Xr")
    phone = int(input("Ingresa el numero del telefono: "))
    if phone >= 1 and phone <= 3:
        iphone(phone)
    else:
        print("Numero invalido")
    
elif marca == 3:
    print("\n1-Huawei P40 Pro, 2-Huawei Mate 40 PRO, 3-Huawei P30 lite")
    phone = int(input("Ingresa el numero del telefono: "))
    if phone >= 1 and phone <= 3:
        huawei(phone)
    else:
        print("Numero invalido")
    
elif marca == 4:
    print("\n1-Xiaomi Redmi Note 10 Pro, 2-Xiaomi Mi Mix 2S, 3-Xiaomi Mi 11 lit")
    phone = int(input("Ingresa el numero del telefono: "))
    if phone >= 1 and phone <= 3:
        xiaomi(phone)
    else:
        print("Numero invalido")
    
elif marca == 5:
    print("\n1-Motorola Moto G60, 2-Motorola Edge 20, 3-Motorola XT2125-4")
    phone = int(input("Ingresa el numero del telefono: "))
    if phone >= 1 and phone <= 3:
        motorola(phone)
    else:
        print("Numero invalido")
    
else:
    print("Numero invalido")
