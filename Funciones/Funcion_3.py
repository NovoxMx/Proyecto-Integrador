def miTelefonos(opcion):
    def miSamsung(opcion_telefono):

        print("\nCelulares Samsung:")
        
        print("Galaxy Note 20 Ultra --- $22,499.00")
        print("Galaxy Z Fold3 5G --- $44,999.00")
        print("Samsung Galaxy A32 --- $5,499.00")

    def miiPhone(opcion_telefono):

        print("\nCelulares iPhone:")
        
        print("iPhone 12 --- $19,499.00")
        print("iPhone 11 Pro Max --- $24,598.00")
        print("iPhone X --- $8,724.00")

    def miHuawei(opcion_telefono):

        print("\nCelulares Huawei:")

        print("Huawei P40 Pro --- $14,999.00")
        print("Huawei Mate 40 PRO --- $25,999.00")
        print("Huawei P30 lite --- $5,639.00")

    def miXiaomi(opcion_telefono):

        print("\nCelulares Xiaomi:")
    
        print("Xiaomi Redmi Note 10 Pro --- $8,399.00")
        print("Xiaomi Mi Mix 2S --- $9,999.00")
        print("Xiaomi Mi 11 lite --- $6,999.00")

    def miMotorola(opcion_telefono):

        print("\nCelulares Motorola:")

        print("Motorola Moto G60 --- $7,299.00")
        print("Motorola Edge 20 --- $10,999.00")
        print("Motorola XT2125-4 --- $13,199.00")

    print("\nSeleccione la marca que le gustaria ver:")
    print("[1]Samsung")    
    print("[2]iPhone") 
    print("[3]Huawei")
    print("[4]Xiaomi") 
    print("[5]Motorola")
    
    opcion_telefono= int(input("Selecciona un numero: "))

    if opcion_telefono == 1:
        miSamsung(opcion_telefono)
    elif opcion_telefono == 2:
        miiPhone(opcion_telefono)
    elif opcion_telefono == 2:
        miHuawei(opcion_telefono)
    elif opcion_telefono == 2:
        miXiaomi(opcion_telefono)
    elif opcion_telefono == 2:
        miMotorola(opcion_telefono)
    else:
        print("Numero invalido")

def miAccesorios(opcion):

    print("\nAccesorios:")
    print("Cargador Tipo C --- $300.00")
    print("Cargador iphone --- $350.00")
    print("Cargador Micro usb --- $200.00")
    print("Audifonos Bluetooth --- $500.00")
    print("Airpod --- $3,899.00")
    print("Fundas --- $500.00")
    print("Protector de pantalla --- $275.00")
    print("Tarjeta de memoria (64Gb) --- $495.00")
    print("Bateria portatil --- $1000.00")
    print("Popsockets ---  $350.00")

print("Bienvenido a los precios de los articulos")
print("Presione: \n[1]Telefonos \n[2]Accesorios ")
opcion= int(input("Selecciona un numero: "))

if opcion == 1:
    miTelefonos(opcion)
elif opcion == 2:
    miAccesorios(opcion)
else:
    ("Numero invalido")