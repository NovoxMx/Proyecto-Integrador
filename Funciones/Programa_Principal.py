#Programa principal que llama a los demás archivos

import os


clear = lambda: os.system('cls')
clear()

marquesina ='》═══════════════════~◈~═══════════════════《'
print(marquesina)
centrar= (len(marquesina))
lesgo = 'Bienvenido al sistema TecCel'
print (lesgo.center(len(marquesina)))
print('\nOpciones disponibles')
print('\n[1]-Mostrar el almacen actual\n[2]-Información de los productos\
    \n[3]-Precio de los productos\n[4]-Registrar de venta\
    \n[5]-Agregar nuevos productos al almacen\n[6]-Informacion de empleados\
    \n[7]-Reporte de ventas\n[8]-Salir' )



opcion = int(input('\nSeleccione la opcion que desee realizar: '))
#print ('\n'+marquesina)
while opcion < 1 or opcion > 8:
    opcion = int(input('Ingrese un número válido: '))
if opcion == 1:
    clear()
    print(marquesina)
    os.system('python Funcionalidad_1.py')
elif opcion == 2:
    clear()
    print(marquesina)
    os.system('python Funcionalidad_2.py')
elif opcion == 3:
    clear()
    print(marquesina)
    os.system('python Funcionalidad_3.py')
elif opcion == 4:
    clear()
    print(marquesina)
    os.system('python Funcionalidad_4.py')
elif opcion == 5:
    clear()
    print(marquesina)
    os.system('python Funcionalidad_5.py')
elif opcion == 6:
    clear()
    print(marquesina)
    os.system('python Funcionalidad_6.py')
elif opcion == 7:
    clear()
    print(marquesina)
    os.system('python Funcionalidad_7.py')
else:
    clear()