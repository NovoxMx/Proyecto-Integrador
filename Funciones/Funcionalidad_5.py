#Agregar productos a almacén 
#André Castillo

def agregar_producto(producto, cantidad):
    almacen_viejo = open("almacenaje.txt", "r")
    lista_almacen = almacen_viejo.readlines()
    print("Antes había: " + lista_almacen[producto * 2])
    num_actualizado = [str(cantidad + int(lista_almacen[producto * 2])) + "\n"]
    nueva_lista = lista_almacen[:(producto * 2)] + num_actualizado + lista_almacen[(producto * 2) + 1:]
    almacen_viejo.close()
    almacen_nuevo = open("almacenaje.txt", "w")
    for renglon in nueva_lista:
        almacen_nuevo.write(renglon)
    almacen_nuevo.close()
    almacen_actualizado = open("almacenaje.txt", "r")
    lista_actualizada = almacen_actualizado.readlines()
    print("Ahora hay: " + lista_actualizada[producto * 2])
    almacen_actualizado.close()
    

print("Secciones:")    #display productos
print("[1] - Telefonos Samsung")
print("[2] - Telefonos iPhone")
print("[3] - Telefonos Huawei")
print("[4] - Telefonos Xiaomi")
print("[5] - Telefonos Motorola")
print("[6] - Accesorios")

categoria = int(input("\n¿En qué sección se encuentra el producto que desea agregar?: "))

if categoria == 1:
    print("\n[1] - Galaxy Note 20 Ultra\n[2] - Galaxy Z Fold3 5G\n[3] - Samsung Galaxy A32")
elif categoria == 2:
    print("\n[1] - iPhone 12\n[2] - iPhone 11 Pro Max\n[3] - iPhone Xr")
elif categoria == 3:
    print("\n[1] - Huawei P40 Pro\n[2] - Huawei Mate 40 PRO\n[3] - Huawei P30 Lite")
elif categoria == 4:
    print("\n[1] - Xiaomi Redmi Note 10 Pro\n[2] - Xiaomi Mi Mix 2S\n[3] - Xiaomi Mi 11 Lite")
elif categoria == 5:
    print("\n[1] - Motorola Moto G60\n[2] - Motorola Edge 20\n[3] - Motorola XT2125-4")
elif categoria == 6:
    print("\n[1] - Cargador Tipo C \n[2] - Cargador iPhone\n[3] - Cargador Micro Usb\n[4] - Audifonos Bluetooth")
    print("[5] - Airpod\n[6] - Fundas\n[7] - Protector de pantalla")
    print("[8] - Tarjeta de memoria (64Gb)\n[9] - Bateria portatil\n[10] - Popsockets\n")

prod = int(input("\nInserte la clave del producto que desea agregar: "))
Cant = int(input("\n¿Qué cantidad de productos desea agregar? "))
while Cant < 1:
    Cant = int(input('Introduzca una cantidad válida: '))

if categoria == 1:
    prod = prod
elif categoria == 2:
    prod = prod + 3
elif categoria == 3:
    prod = prod + 6
elif categoria == 4:
    prod = prod + 9
elif categoria == 5:
    prod = prod + 12
elif categoria == 6:
    prod = prod + 15

agregar_producto(prod, Cant)