#Funcion 7 orientada hacia algún administrador
#Trabajada por: André Castillo - A01254180
import csv
import os
clear = lambda: os.system('cls')
def imprimir_registro():
    registro = open("registro.txt", "r")
    lista_registro = registro.readlines()
    for renglon in lista_registro:
        print(renglon)
    registro.close()

def imprimir_registro_empleado(n_empleado):
    registro = open("ventas_empleados.txt", "r")
    lista_registro = registro.readlines()
    print(str(lista_registro[(n_empleado * 2) - 1]) + "Ha vendido: $" + lista_registro[n_empleado * 2])
    bonos = (float(lista_registro[n_empleado * 2]) * .05)
    print("Bonos: $" + str(round(bonos, 2)))
    registro.close()


print('---Bienvenido al reporte de ventas.---\n[1] - Registro de ventas\n[2] - Ventas por empleado')
option = int(input("Ingrese lo que desee hacer: "))

if option == 1:
    imprimir_registro()
elif option == 2:
    print('\nEmpleado: 1-Jose, 2-Pepesio, 3-Pablo')
    a_1 = int(input('Ingrese su numero de empleado: '))
    while a_1 < 1 or a_1 >3:
        a_1 = int(input('Ingrese un número válido: '))
    print("")
    imprimir_registro_empleado(a_1)

    
print('\n•❅ ────────────✧ ❅ ✦ ❅ ✧──────────── ❅ •')    
sino = int(input('\n¿Desea salir o volver al menú principal?\
        \n[1]-Salir \n[2]-Volver al menú principal\n'))
while sino < 1 or sino > 2:
        sino = int(input('Ingrese un número válido: '))
if sino == 2:
    os.system('python Programa_Principal.py')
else:
    clear()
