# Función 4 - Registro de ventas
# Función trabajada por - Marco Montoya A 01254155

from datetime import date
from datetime import datetime

hora = datetime.now()
registro = []
print('Bienvenido al registro, ingrese lo que se le pide.')
print('Empleado: \n1. Jose \n2. Pablo \n3. Pedro')
a_1 = int(input())
emp = str(0)
if a_1 == 1:
    emp = 'Jose'
elif a_1 == 2:
    emp= 'Pablo'
elif a_1 == 3:
    emp = 'Pedro'
else:
    print('Introduzca un número valido')

print (emp)
print(hora)