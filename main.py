"""
GRUPO 5: Miselli Martín, Quiroga Christian y Maestrelli Dante.
Crear un programa para el manejo administrativo de un club de deportes (3 deportes
diferentes) teniendo en cuenta los siguientes aspectos:
1) El sistema debe ser de acceso restringido sólo para algunas opciones especiales (a
considerar según el grupo de trabajo)
2) Cuotas sociales y deportivas, socios y no socios, invitados
3) Salida de comprobantes por pantalla.
4) Rendición de cuentas mensuales
"""

from Conexion import *
from funciones import *
from entidades import *

#Programa principal

op = 0
rol = ""
while op != 2:
    op = menu_login()
    if op == 1:
        Usuario.usuario = input("Ingrese usuario: ")
        Usuario.password = input("Ingrese password: ")
        
        resultado = Usuario.iniciar_sesion(Usuario.usuario, Usuario.password)

        if resultado[2]== 1:
            op1 = menu_gestion_empleado()
           
            while op1 != 5:
                op1 = menu_gestion_empleado()
                if op1 == 1:
                    print("***Dar de alta un Socio***")
                    nombre = input("Ingrese el nombre: ")
                    Usuario.alta(nombre)
                elif op1 == 2:
                    print("***Dar de baja un socio***")
                    Usuario.baja()
                elif op1 == 3:
                    print("Modificar los datos de un socio")
                    Usuario.modificar()
                elif op1 == 4:
                    print("***Lista de Socios***\n")
                    Usuario.lista()  
                else:
                    print("FIN!")
        elif  resultado[2]== 2:
            op1 = menu_gestion_gerente()
            if op1 == 1:
                print("***Dar de alta un Socio***")
                nombre = input("Ingrese el nombre: ")
                Usuario.alta(nombre)
            elif op1 == 2:
                print("***Dar de baja un socio***")
                Usuario.baja()
            elif op1 == 3:
                print("Modificar los datos de un socio")
                Usuario.modificar()
            elif op1 == 4:
                print("***Lista de Socios***\n")
                Usuario.lista() 
            elif op1 == 5:
                print("Mostrar informe mensual")
                Usuario.mostrar_informe() 
            else:
                print("FIN!")
        else:
            print("El usuario o el password es incorrecto!")

    else:
        print("FIN!")
        break
    

op1 = 0
while op1 != 6:
    op1 = menu_gestion_empleado()
    if op1 == 1:
        print("***Dar de alta un Socio***")
        nombre = input("Ingrese el nombre: ")
        Usuario.alta(nombre)
    elif op1 == 2:
        print("***Dar de baja un socio***")
        Usuario.baja()
    elif op1 == 3:
        print("Modificar los datos de un socio")
        Usuario.modificar()
    elif op1 == 4:
        print("***Lista de Socios***\n")
        Usuario.lista()  
    else:
        print("FIN!")

