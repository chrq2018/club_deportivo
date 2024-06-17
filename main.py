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
import getpass
#Programa principal

op3 = 0
rol = ""
while op3 != 2:
    op3 = menu_login()
    if op3 == 1:
        resultado = validar_inicio_sesion()
        if resultado != None:
            if resultado[3] == 1:
                op2 = 0
                while op2 != 5:
                    op2 = menu_gestion_empleado()
                    if op2 == 1:
                        print("***Dar de alta un Socio***")
                        nombre = input("Ingrese el nombre: ")
                        Usuario.alta(nombre)
                    elif op2 == 2:
                        print("***Dar de baja un socio***")
                        Usuario.baja()
                    elif op2 == 3:
                        print("Modificar los datos de un socio")
                        Usuario.modificar()
                    elif op2 == 4:
                        print("***Lista de Socios***\n")
                        Usuario.lista()  
                    else:
                        print("Volver al menu login!")
                        
            elif  resultado[3]== 2:
                op2 = 0
                while op2 != 6:
                    op2 = menu_gestion_gerente()
                    if op2 == 1:
                        print("***Dar de alta un Socio***")
                        nombre = input("Ingrese el nombre: ")
                        Usuario.alta(nombre)
                    elif op2 == 2:
                        print("***Dar de baja un socio***")
                        Usuario.baja()
                    elif op2 == 3:
                        print("Modificar los datos de un socio")
                        Usuario.modificar()
                    elif op2 == 4:
                        print("***Lista de Socios***\n")
                        Usuario.lista()  
                    elif op2 == 5:
                        print("Mostrar informe mensual")
                        Usuario.mostrar_informe() 
                    else:
                        print("Volver al menu login!")
        else:
            op3 = 2
else:
    print("FIN!")
        