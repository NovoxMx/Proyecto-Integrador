#Agregar productos a almacén 
#André Castillo ya la apartó ingatu

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
    

#display productos
#Ejemplo_1:
print("[1] - Iphone 11")

"""Galaxy Note 20 Ultra
Galaxy Z Fold3 5G
Samsung Galaxy A32
iPhone 12
iPhone 11 Pro Max
iPhone Xr
Huawei P40 Pro
Huawei Mate 40 PRO
Huawei P30 Lite
Xiaomi Redmi Note 10 Pro
Xiaomi Mi Mix 2S
Xiaomi Mi 11 Lite
Motorola Moto G60
Motorola Edge 20
Motorola XT2125-4
Cargador Tipo C 
Cargador iPhone
Cargador Micro Usb
Audifonos Bluetooth
Airpod
Fundas
Protector de pantalla
Tarjeta de memoria (64Gb)
Bateria portatil
Popsockets"""

prod = int(input("Inserte la clave del producto que desea agregar: "))

Cant = int(input("¿Qué cantidad de productos desea agregar? "))

agregar_producto(prod, Cant)