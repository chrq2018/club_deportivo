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

from conexion import *
from consultas import *
from funciones import *

#Programa principal
conexion = conexion_sql_server()

opcion = 0
while opcion != 5:
    opcion = menu()
    if opcion == 1:
        print("Ingrese los datos del Socio\n")
        nombre = input("Ingrese el nombre: ")
        alta(nombre, conexion)
        
    elif opcion == 2:
        print("Modificar los datos de un socio")
        modificar(conexion)
        
    elif opcion == 3:
        print("Modificar los datos de un socio")
        baja(conexion)  
        
    elif opcion == 4:
        print("Lista de Socio\n")
        lista(conexion)
        
    else:
        conexion.close()
        print("FIN!")

