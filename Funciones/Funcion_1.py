#función de inventario en forma de lista con: tipo de artículo y cantidad, marcar cuando hay menos de 5 en existencia.
#función por: Marco Tulio Montoya Angulo - A01254155
#def almacenamiento():
print('Bienvenido al inventario, seleccione una opción: ')
print ('[1] Si desea ver el inventario de dispositivos.')
print ('[2] Si desea ver el inventario de otros.')
opcion = int(input())

if opcion < 1 or opcion >2:
    print ('Ingrese un número valido.')
    
elif opcion == 1:
    almacenamiento = open('almacenaje.txt', "r")
    while True:
        theline = almacenamiento.readline()
        
        if len (theline) == 0:
            break
        print(theline, end ="")
elif opcion == 2:
    print('Inventario 2')