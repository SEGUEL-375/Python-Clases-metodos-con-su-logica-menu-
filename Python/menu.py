
from libreta import Libreta
from contacto import *
libreta = Libreta();
respuesta = 0
while (respuesta <= 4):
    print("BIENVENIDO:")
    print("--------------------")
    print("(1) Añadir Contacto")
    print("(2) Lista de Contactos")
    print("(3) Buscar contactos")
    print("(4) SALIR")
    print("--------------------")
    respuesta = int(input("Ingrese su respuesta:"))
    print("")
    print("--------------------")
    if respuesta == 1:
        print("")
        nombre=input("Ingrese nombre de contacto:")
        apellido=input("Ingrese apellido del contacto:")
        celular=input("Ingrese numero de celular:")
        gmail=input("Ingrese gmail del contacto:")
        contacto1=Contacto(nombre,apellido,celular,gmail)
        libreta.añadir_Contacto(contacto1)
        
    elif respuesta == 2:
        libreta.lista_de_Contacto()
            
    elif respuesta == 3:
        nombre=input("Ingrese nombre del contacto a buscar:")
        apellido= input("Ingrese el apellido del contacto a buscar:")
        print(libreta.buscar_Contacto(nombre,apellido))
        
    elif respuesta == 4:
        respuesta= 5
    else:
        print("usted ingreso respuesta una incorrecta")