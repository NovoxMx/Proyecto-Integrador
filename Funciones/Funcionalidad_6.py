#Empleados y agreagar a empleados
#Por Angel Marin
import csv
import os
clear = lambda: os.system('cls')

print("Empleados")
print("Que quiere hacer: \n[1]Agregar Nuevo empleado. \n[2]Mostrar a los empleados.")
valor= int(input("Elegir: "))

#Agregar nuevos empleados
while valor < 1 or valor > 2:
    valor = int(input('Ingrese un número válido: '))

if valor == 1:
    contraseña = input('Ingrese la contraseña: ')
    if contraseña != '3.14159265358979323846264338327950288419716939937510582097494':
        print ('Contraseña incorrecta')

    else:
        archivo= open("Empleados.csv", "a")
        #Esa es mi direccion al archivo, si lo quieren cambiar haganlo
        nombre= input("Nombre del empleado: ")
        apellido= input("Apellido del empleado: ")
        edad= input("Introduce la edad: ")
        horario= input("Horario de trabajo: ")
        dia_Descanso= input("Dia de Descanso: ")

        archivo.write(apellido)
        archivo.write(",")
        archivo.write(nombre)
        archivo.write(",")
        archivo.write(edad)
        archivo.write(",")
        archivo.write(horario)
        archivo.write(",")
        archivo.write(dia_Descanso)
        archivo.write("\n")
        archivo.close()
    
    sino = int(input('\n¿Desea salir o volver al menú principal?\
                \n[1]-Salir \n[2]-Volver al menú principal\n'))
    while sino < 1 or sino > 2:
            sino = int(input('Ingrese un número válido: '))
    if sino == 2:
        os.system('python Programa_Principal.py')
    else:
        clear()

#Lista de usuarios
elif valor == 2:
    print("Empleados: \n")

    with open("Empleados.csv", newline= '') as csvfile:
        archivo1=  csv.reader(csvfile, delimiter=',')

        for filas in archivo1:
            print (filas)
    
print('\n•❅ ────────────✧ ❅ ✦ ❅ ✧──────────── ❅ •')
sino = int(input('\n¿Desea salir o volver al menú principal?\
                \n[1]-Salir \n[2]-Volver al menú principal\n'))
while sino < 1 or sino > 2:
    sino = int(input('Ingrese un número válido: '))
if sino == 2:
    os.system('python Programa_Principal.py')
else:
    clear()

