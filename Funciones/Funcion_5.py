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
print("[2] - Samsung x")

prod = int(input("Inserte la clave del producto que desea agregar: "))

Cant = int(input("¿Qué cantidad de productos desea agregar? "))

agregar_producto(prod, Cant)