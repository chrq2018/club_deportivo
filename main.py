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
import getpass
#Programa principal
op3 = 0
rol = ""
while op3 != 2:
    op3 = menu_login()
    if op3 == 1:
        resultado = validar_inicio_sesion()
        if resultado != None:
            if resultado[3] == 'Empleado':
                op2 = 0
                while op2 != 7:
                    op2 = menu_gestion_empleado()
                    if op2 == 1:
                        print("***Registrar pagos***\n")
                        mes = int(input("Ingrese el mes: "))
                        anio = int(input("Ingrese el anio: "))
                        monto = float(input("Ingrese el monto: "))
                        tipo_de_cuota = int(input("Ingrese el tipo de cuota: "))
                        id_cliente = int(input("Ingrese el id_cliente: "))
                        registrar_pago(mes, anio, monto, tipo_de_cuota, id_cliente) 
                        mostrar_comprobante_pago(id_cliente, mes) 
                    elif op2 == 2:
                        id_cliente = int(input("Ingrese el id_cliente: "))
                        mes = int(input("Ingrese el mes: "))
                        mostrar_comprobante_pago(id_cliente, mes)    
                    elif op2 == 3:
                        print("***Dar de alta un Socio***")
                        nombre = input("Ingrese el nombre: ")
                        apellido = input("Ingrese el apellido: ")
                        telefono = input("Ingrese el telefono: ")
                        deporte = int(input("Ingrese el deporte: "))
                        tipo_de_cliente = int(input("Ingrese el tipo de cliente: "))
                        alta(nombre, apellido, telefono, deporte, tipo_de_cliente)
                    elif op2 == 4:
                        print("***Dar de baja un socio***")
                        while True:
                            eliminar = input("\nQuiere eliminar un socio s/n: ")
                            if eliminar.lower() == "s":
                                baja()
                            else:
                                print("Salio de la opcion Baja")
                                break    
                    elif op2 == 5:
                        print("Modificar los datos de un socio")
                        while True:
                            actualizar = input("\nQuiere actualizar un dato s/n: ")
                            if actualizar.lower() == "s":
                                modificar()
                            else:
                                print("Salio de la opcion modificar")
                                break
                    elif op2 == 6:
                        print("***Lista de Socios***\n")
                        lista()  
                    else:
                        print("Volver al menu login!")

            elif  resultado[3]== 'Administrador':
                op2 = 0
                while op2 != 9:
                    op2 = menu_gestion_gerente()
                    if op2 == 1:
                        print("***Registrar pagos***\n")
                        mes = int(input("Ingrese el mes: "))
                        anio = int(input("Ingrese el anio: "))
                        monto = float(input("Ingrese el monto: "))
                        tipo_de_cuota = int(input("Ingrese el tipo de cuota: "))
                        id_cliente = int(input("Ingrese el id_cliente: "))
                        registrar_pago(mes, anio, monto, tipo_de_cuota, id_cliente)
                        mostrar_comprobante_pago(id_cliente, mes)
                    elif op2 == 2:
                        id_cliente = int(input("Ingrese el id_cliente: "))
                        mes = int(input("Ingrese el mes: "))
                        mostrar_comprobante_pago(id_cliente, mes) 
                    elif op2 == 3:
                        mostrar_pagos()
                    elif op2 == 4:
                        print("***Dar de alta un Socio***")
                        nombre = input("Ingrese el nombre: ")
                        apellido = input("Ingrese el apellido: ")
                        telefono = input("Ingrese el telefono: ")
                        deporte = ''
                        while True:
                            deporte = input("Ingrese el nuevo deporte: ")
                            if deporte in ['Fútbol', 'Básquet', 'Tenis']:
                                break
                            else:
                                print("El deporte ingresado debe ser 'Fútbol', 'Básquet' o 'Tenis'")
                        tipo_de_cliente = ''
                        while True:
                            tipo_de_cliente = input("Ingrese el tipo de cliente: ")
                            if tipo_de_cliente in ['Socio', 'No socio', 'Invitado']:
                                break
                            else:
                                print("El tipo de cliente ingresado debe ser 'Socio', 'No socio' o 'Invitado'")
                        alta(nombre, apellido, telefono, deporte, tipo_de_cliente)
                    elif op2 == 5:
                        print("***Dar de baja un socio***")
                        while True:
                            eliminar = input("\nQuiere eliminar un socio s/n: ")
                            if eliminar.lower() == "s":
                                baja()
                            else:
                                print("Salio de la opcion Baja")
                                break    
                    elif op2 == 6:
                        print("Modificar los datos de un cliente")
                        while True:
                            actualizar = input("\nQuiere actualizar un dato s/n: ")
                            if actualizar.lower() == "s":
                                modificar()
                                print('Cliente modificado')
                            else:
                                print("Salio de la opcion modificar")
                                break
                    elif op2 == 7:
                        print("***Lista de Socios***\n")
                        lista()  
                    elif op2 == 8:
                        print("Mostrar informe mensual")
                        mostrar_informe() 
                    else:
                        print("Volver al menu login!")      
        else:
            op3 = menu_login()
else:
    print("FIN!")
        