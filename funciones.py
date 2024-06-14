import pyodbc
from Conexion import *

def menu_gestion_empleado():
    print()
    opc = 0
    while opc < 1 or opc > 5:
        print()
        print('1) Alta')
        print('2) Baja')
        print('3) Modificar')
        print('4) Listar')
        print('5) Salir')
        opc = int(input('Elija una opción correcta: '))
    return opc

def menu_gestion_gerente():
    print()
    opc = 0
    while opc < 1 or opc > 5:
        print()
        print('1) Alta')
        print('2) Baja')
        print('3) Modificar')
        print('4) Listar')
        print('5) Impromir Informes')
        print('6) Salir')
        opc = int(input('Elija una opción correcta: '))
    return opc

def menu_login():
    print()
    opc = 0
    while opc < 1 or opc > 2:
        print("****Login****")
        print('1) Inicio')
        print('2) Salir')
        opc = int(input('Elija una opción correcta: '))
    return opc
        

