#Empleados y agreagar a empleados
#Por Angel Marin
import csv

print("Empleados")
print("Que quiere hacer: \n[1]Agregar Nuevo empleado. \n[2]Mostrar a los empleados.")
valor= int(input("Elegir: "))

#Agregar nuevos empleados
if valor == 1:
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

#Lista de usuarios
elif valor == 2:
    print("Empleados: \n")

    with open("Empleados.csv", newline= '') as csvfile:
        archivo1=  csv.reader(csvfile, delimiter=',')

        for filas in archivo1:
            print (filas)


