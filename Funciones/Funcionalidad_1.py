#función de inventario en forma de lista con: tipo de artículo y cantidad, marcar cuando hay menos de 5 en existencia.
#función por: Marco Tulio Montoya Angulo - A01254155
#def almacenamiento():
import os
clear = lambda: os.system('cls')
print('Bienvenido al inventario, seleccione una opción: ')

almacenamiento = open('almacenaje.txt', "r")
while True:
    theline = almacenamiento.readline()
        
    if len (theline) == 0:
        break
    print(theline, end ="")

print('\n•❅ ────────────✧ ❅ ✦ ❅ ✧──────────── ❅ •')
print('\n¿Desea salir o volver al menú principal?\
    \n[1]-Salir \n[2]-Volver al menú principal')

sino = int(input(''))
while sino < 1 or sino > 2:
    sino = int(input('Ingrese un número válido: '))
if sino == 2:
    os.system('python Programa_Principal.py')
else:
    clear()
