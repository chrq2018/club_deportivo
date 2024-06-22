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
from funciones import *
from os import system
#Programa principal
op3 = 0
rol = ""
while op3 != 2:
    print("****************************************************************")
    print("* Bienvenido al sistema de gestión administrativo para el Club *")
    print("****************************************************************")
    print()
    op3 = menu_login()
    if op3 == 1:
        resultado = validar_inicio_sesion()
        if resultado != None:
            rol = resultado[3]
            menu_principal(rol) 
        else:
            op3 = menu_login()
    if op3 == 2:
        print("************************************************************")
        print("*           Gracias por utilizar nuestro sistema           *")
        print("************************************************************")
        