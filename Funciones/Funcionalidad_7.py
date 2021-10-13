#Funcion 7 orientada hacia algún administrador

def imprimir_registro():
    registro = open("registro.txt", "r")
    lista_registro = registro.readlines()
    for renglon in lista_registro:
        print(renglon)
    registro.close()
