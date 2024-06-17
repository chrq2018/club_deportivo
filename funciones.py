import pyodbc
from Conexion import *
from entidades import *
import getpass

def menu_gestion_empleado():
    print()
    opc = 0
    while opc < 1 or opc > 5:
        print()
        print('1) Alta')
        print('2) Baja')
        print('3) Modificar')
        print('4) Listar')
        print('5) Volver al menu login!')
        opc = int(input('Elija una opción correcta: '))
    return opc
    print()

def menu_gestion_gerente():
    print()
    opc = 0
    while opc < 1 or opc > 6:
        print()
        print('1) Alta')
        print('2) Baja')
        print('3) Modificar')
        print('4) Listar')
        print('5) Impromir Informes')
        print('6) Volver al menu login!')
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
        
def validar_inicio_sesion():
        cont = 1
        while cont <= 3:   
            usuario = input("Ingrese usuario: ")
            #password = input("Ingrese password: ")
            cantLetras = 2
            password = getpass.getpass("Enter your password: ")
            while len(password) < cantLetras: 
                password = getpass.getpass("Enter your password (cantidad de caracteres debe ser mayor a 2): ")
            resultado = Usuario.iniciar_sesion(usuario, password)
            if resultado:
                print("Ingreso correcto")
                cont = 4
            else:
                print("Los datos ingresados son incorrectos")
                if cont == 3:
                    print("Usuario bloqueado, comuniquese con el administrador del sistema!!")    
                cont += 1 
        return resultado