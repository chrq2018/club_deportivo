import pyodbc
import getpass 
import datetime
from os import system

def conexion_sql_server():
    try:
        conexion = 'DRIVER={SQL SERVER}; SERVER=MARIANA\SQLEXPRESS;DATABASE=CLUB_DEPORTIVO;Trust_Connection={yes}; UID=sa; PWD=123'                    
    except ConnectionError as e:
                print("Ocurrio un error al conectar SQL Server: ", e)
    return conexion

def menu_login():
    print()
    opc = 0
    while True:
        print("*********************************")
        print("*             LOGIN             *")
        print("*********************************")
        print()
        print('1) Inicio')
        print('2) Salir')
        opc = input('Elija una opción correcta: ')
        print()
        if opc == '1' or opc == '2':
            return int(opc)
        

def menu_gestion_empleado():
    print()
    opc = 0
    while True:
        print()
        print('1) Volver al menu login!')
        print('2) Alta clientes')
        print('3) Baja clientes')
        print('4) Modificar cliente')
        print('5) Buscar cliente')
        print('6) Listar clientes')
        print('7) Registrar pagos')
        print('8) Mostrar comprobante de pago')
        opc = input('Elija una opción correcta: ')
        if opc in ['1','2','3','4','5','6','7','8']:
            return int(opc)

def menu_gestion_gerente():
    print()
    opc = 0
    while True:
        print()
        print('1) Volver al menu login!')
        print('2) Alta clientes')
        print('3) Baja clientes')
        print('4) Modificar cliente')
        print('5) Buscar cliente')
        print('6) Listar clientes')
        print('7) Registrar pagos')
        print('8) Mostrar comprobante de pago')
        print('9) Mostrar pagos')
        print('10) Imprimir informes')
        opc = input('Elija una opción correcta: ')
        if opc in ['1','2','3','4','5','6','7','8','9','10']:
            return int(opc)

def menu_principal(rol):
    op2 = 0
    while op2 != 11:
        if rol=='Empleado': op2 = menu_gestion_empleado()
        if rol=='Administrador':
            op2 = menu_gestion_gerente()
            if op2 == 9: mostrar_pagos()
            if op2 == 10: mostrar_informe()

        if op2 == 1:
            break
        elif op2 == 2:
            print()
            alta()
        elif op2 == 3:
            print()
            print("***   DAR DE BAJA UN CLIENTE   ***")
            while True:
                eliminar = input("\nQuiere eliminar un cliente s/n: ")
                if eliminar.lower() == "s":
                    baja()
                    break
                else:
                    print("Salio de la opcion Baja")
                    break    
        elif op2 == 4:
            print()
            print("***   MODIFICAR DATOS DE UN CLIENTE   ***")
            while True:
                actualizar = input("\nQuiere actualizar un dato s/n: ")
                if actualizar.lower() == "s":
                    modificar()
                    break
                else:
                    print("Salio de la opcion modificar")
                    break
        elif op2 == 5:
            print()
            ver_cliente()
        elif op2 == 6:
            print()
            lista() 
        elif op2 ==7:
             print()
             registrar_pago()
        elif op2 ==8:
            print()
            print("***   MOSTRAR COMPROBANTE   ***")
            id_cliente = int(input("Ingrese el id_cliente: "))
            mes = int(input("Ingrese el mes: "))
            mostrar_comprobante_pago(id_cliente, mes) 

def input_validado(mensaje):
    valor = ''
    while True:
        valor = input(mensaje)
        if len(valor) >= 3:
            return valor
        else:
            print("Debe ingresar al menos 3 caracteres")
        
def registrar_pago():
    print("***   REGISTRAR PAGOS   ***\n")
    mes = 0
    while True:
        try:
            mes = int(input("Ingrese el mes: "))
            if mes >= 1 and mes <=12:
                break
            else:
                print("El mes ingresado debe estar entre 1 y 12")
        except:
            print("El mes ingresado debe estar entre 1 y 12")
    anio = 0
    while True:
        try:
            anio = int(input("Ingrese el año: "))
            fecha_actual = datetime.datetime.now()
            anio_actual = fecha_actual.year
            if anio > 1900 and anio <= anio_actual:
                break
            else:
                print("El año ingresado debe ser un número mayor a 1900 y no mayor al año actual")
        except:
            print("El año ingresado debe ser un número")
    id_cliente = 0
    while True:
        try:
            id_cliente = int(input("Ingrese el id del cliente: "))
            if id_cliente:
                break
        except:
            print("El id debe ser un número")
    tipo_de_cuota = ''
    monto = 0
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sqlId = "SELECT tipo_de_cliente, deporte FROM Clientes WHERE id_cliente = ?;"
        cursor.execute(sqlId, id_cliente)
        cliente, deporte = cursor.fetchone()
        if cliente == 'Invitado':
            print("Los invitados no pueden registrar pagos.")
            return
        if deporte == None:
            tipo_de_cuota = 'Social'
        else:
            tipo_de_cuota = 'Deportiva'
        if cliente == 'Socio' and tipo_de_cuota == 'Deportiva':
            monto = 7500
        if cliente == 'Socio' and tipo_de_cuota == 'Social':
            monto = 10000
        if cliente == 'No socio' and tipo_de_cuota == 'Deportiva':
            monto = 12500
        if cliente == 'No socio' and tipo_de_cuota == 'Social':
            monto = 15000
        sql = "INSERT INTO Pagos (mes, anio, monto, tipo_de_cuota, id_cliente) values (?, ?, ?, ?, ?);"
        valores = (mes, anio, monto, tipo_de_cuota, id_cliente)
        cursor.execute(sql,valores)
        conn.commit()
        print(cursor.rowcount,"Registro ingresado") 
        if monto != 0:
            sql2 = "UPDATE Clientes SET estado = 'Activo' WHERE id_cliente = ?"
            cursor.execute(sql2, id_cliente)
            conn.commit()
        mostrar_comprobante_pago(id_cliente, mes)
        conn.close()
    except Exception as e:
        print("Error!, no se pudo registrar el pago{}".format(e))

def mostrar_comprobante_pago(id_cliente, mes):
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = f"""SELECT *
                 from Pagos 
                 where id_cliente = ? and mes = ? ;"""
        valores = (id_cliente, mes)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()
        if resultado:
            print("------------------------------")
            print("|*** COMPROBANTE DE PAGO  ***|")
            print("------------------------------")
            print("|Cliente:     {:<15}|".format(resultado[5]))
            print("|Cuota:       {:<15}|".format(resultado[4]))
            print("|Mes:         {:<15}|".format(resultado[1]))
            print("|Año:         {:<15}|".format(resultado[2]))
            print("|Importe:     {:<15}|".format(resultado[3]))
            print("------------------------------")
        else: 
            print(f"No se encontró un comprobante para el cliente {id_cliente} en el mes {mes}")
    except Exception as e:
        print("Error!, no se pudo registrar el pago{}".format(e))

def mostrar_pagos():
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "SELECT * FROM Pagos;"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print()
        print("---------------------------------------------------------------")
        print("|           ***   LISTADO DE TODOS LOS PAGOS   ***            |")
        print("---------------------------------------------------------------")
        print("|Pago  |  Mes |  Año  |   Monto   |   Tipo de cuota  | Cliente|")
        print("---------------------------------------------------------------")
        for pago in resultado:
            #print(f'Pago: {pago[0]}, Mes: {pago[1]}, Año: {pago[2]}, Monto: {pago[3]}, Tipo de cuota: {pago[4]}, Cliente: {pago[5]} \n')
            print("|{:^5}|{:^6}|{:^8}|{:^11}|{:^18}|{:^8}|".format(pago[0],pago[1],pago[2],pago[3],pago[4],pago[5]))
            print("---------------------------------------------------------------")
        conn.close()
    except Exception as e:
        print("Error!, no se puden mostrar los pagos {}".format(e))

def alta():
    print()
    print("*** DAR DE ALTA UN CLIENTE ***")
    nombre = input_validado("Ingrese el nombre: ")
    apellido = input_validado("Ingrese el apellido: ")
    telefono = 0
    while True:
        try:
            telefono = int(input("Ingrese el teléfono: "))
            if telefono:
                break
        except:
            print("El teléfono debe ser numérico")
    deporte = None
    while True:
        deporte = input("Ingrese el nuevo deporte (opcional): ")
        if deporte in ['Fútbol', 'Básquet', 'Tenis', '']:
            if deporte == '': deporte = None
            break
        else:
            print("El deporte ingresado debe ser 'Fútbol', 'Básquet', 'Tenis' o ninguno ")
    tipo_de_cliente = ''
    while True:
        tipo_de_cliente = input("Ingrese el tipo de cliente: ")
        if tipo_de_cliente in ['Socio', 'No socio', 'Invitado']:
            break
        else:
            print("El tipo de cliente ingresado debe ser 'Socio', 'No socio' o 'Invitado'")
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "INSERT INTO Clientes (nombre, apellido, telefono, deporte, tipo_de_cliente) values (?, ?, ?, ?, ?);"
        valores = (nombre, apellido, telefono, deporte, tipo_de_cliente)
        cursor.execute(sql,valores)
        conn.commit()
        print(cursor.rowcount,"Registro ingresado")
        conn.close()
    except Exception as e:
        print("Error!, no se pudo dar de alta{}".format(e))

def baja():
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "SELECT * FROM Clientes WHERE estado != 'Inactivo';"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print("-------------------------------------------")
        print("|Cliente |     Nombre     |   Apellido    |")
        print("-------------------------------------------")
        for cliente in resultado:
            print("|{:^8}|{:^16}|{:^15}|".format(cliente[0],cliente[1],cliente[2]))
            print("-------------------------------------------")
        print()
        idS = 0
        while True:
            try:
                idS = int(input("Ingrese el id del cliente que desea eliminar: "))
                if idS:
                    break
            except:
                print("El id debe ser un número")
        consultaV ="SELECT id_cliente, nombre, apellido from Clientes where id_cliente = ?;"
        cursor.execute(consultaV, idS)
        idCliente, nombreCliente, apellidoCliente = cursor.fetchone()
        if resultado:
            consultaD = "UPDATE Clientes SET estado = 'Inactivo' WHERE id_cliente = ?;"
            cursor.execute(consultaD, (idCliente))
            conn.commit()
            print(f"El cliente {nombreCliente} {apellidoCliente} ha pasado a ser inactivo.")
        else:
            print("El ID ingresado es incorrecto!!")
        conn.close()
    except Exception as e:
        print("Error!, no se pudo realizar la baja{}".format(e))

def modificar():
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "SELECT * FROM Clientes;"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print("---------------------------------------------------------")
        print("|Cliente |     Nombre     |   Apellido    |   Deporte   |")
        print("---------------------------------------------------------")
        for cliente in resultado:
            if cliente[4] == None:
                cliente[4] = ""
            print("|{:^8}|{:^16}|{:^15}|{:^13}|".format(cliente[0], cliente[1], cliente[2], cliente[4]))
            print("---------------------------------------------------------")
        
        idS = 0
        while True:
            try:
                idS = int(input("Ingrese el id del cliente que desea actualizar: "))
                #if idS:
                 #   break
            except ValueError:
                print("\nEl ID debe ser un número!")

            sql = "SELECT id_cliente FROM Clientes WHERE id_cliente = ?;"
            cursor.execute(sql, idS)
            resultado = cursor.fetchone()
            if resultado:
                
                try:
                    nombre = input("Ingrese el nuevo nombre (deje en blanco para no modificar): ").strip()
                    apellido = input("Ingrese el nuevo apellido (deje en blanco para no modificar): ").strip()
                    deporte = input("Ingrese el nuevo deporte (deje en blanco para no modificar): ").strip()

                    if deporte not in ['Fútbol', 'Básquet', 'Tenis', '']:
                        print("El deporte ingresado debe ser 'Fútbol', 'Básquet', 'Tenis' o ninguno ")
                    else:                                                     

                        query = "UPDATE Clientes SET "
                        parameters = []

                        if nombre:
                            query += "nombre = ?, "
                            parameters.append(nombre)
                        if apellido:
                            query += "apellido = ?, "
                            parameters.append(apellido)
                        if deporte:
                            query += "deporte = ?, "
                            parameters.append(deporte)


                        query = query.rstrip(", ") + " WHERE id_cliente = ?"
                        parameters.append(idS)

                        cursor.execute(query, parameters)
                        conn.commit()
                        print("\nCliente actualizado correctamente.\n")
                        break                    
                except:
                    print("\nNo se actualizó ningún dato.\n")
                    return
                        
                    
            else:
                print("\nEl ID ingresado es incorrecto!\n")

        conn.close()
    except Exception as e:
        print("\nError!, no se pudo realizar la modificación: {}".format(e))



def lista():
    print("***   LISTADO DE CLIENTES   ***")
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "SELECT * FROM Clientes;"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print("----------------------------------------------------------------------------------------------------")
        print("|Cliente |     Nombre     |   Apellido    |   Telefono  |   Deporte   |  Tipo de cuota  |  Estado  |")
        print("----------------------------------------------------------------------------------------------------")
        for cliente in resultado:
            if cliente[4] == None:
                cliente[4] = ""
            if cliente[6] == None:
                cliente[6] = ""
            print("|{:^8}|{:^16}|{:^15}|{:^13}|{:^12}|{:^18}|{:^10}|".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4],cliente[5],cliente[6]))
            print("----------------------------------------------------------------------------------------------------")
        conn.close()
    except Exception as e:
        print("Error!, no se pudo mostrar los clientes{}".format(e))

def ver_cliente():
    print("***   BUSCAR UN CLIENTE   ***")
    try:
        idS = input_validado("\nIngrese el apellido o nombre del cliente que desea buscar: ")
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "SELECT * FROM Clientes WHERE apellido LIKE ? OR nombre LIKE ?;"
        cursor.execute(sql, ('%' + idS + '%', '%' + idS + '%'))
        resultado = cursor.fetchall()
        print("----------------------------------------------------------------------------------------------------")
        print("|Cliente |     Nombre     |   Apellido    |   Telefono  |   Deporte   |  Tipo de cuota  |  Estado  |")
        print("----------------------------------------------------------------------------------------------------")
        if resultado:
            for cliente in resultado:
                if cliente[4] == None:
                    cliente[4] = ""
                if cliente[6] == None:
                    cliente[6] = ""
                print("|{:^8}|{:^16}|{:^15}|{:^13}|{:^12}|{:^18}|{:^10}|".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4],cliente[5],cliente[6]))
                print("----------------------------------------------------------------------------------------------------")
        else:
            print(f"No se ha encontrado al cliente: {idS}")
        conn.close()
    except Exception as e:
        print("Error!, no se pudo mostrar a los clientes{}".format(e))


def validar_inicio_sesion():
        cont = 1
        while cont <= 3:   
            usuario = input_validado("Ingrese usuario: ")
            #password = input("Ingrese password: ")
            cantLetras = 2
            password = getpass.getpass("Ingrese password: ")
            """while len(password) < cantLetras: 
                password = getpass.getpass("Ingrese password (cantidad de caracteres debe ser mayor a 2): ")"""
            resultado = iniciar_sesion(usuario, password)
            if resultado:
                print(f"Bienvenido {resultado[1]}. Ingresó al sistema como {resultado[3]}.")
                cont = 4
            else:
                print("Los datos ingresados son incorrectos")
                if cont == 3:
                    print("Usuario bloqueado, comuniquese con el administrador del sistema!!")    
                cont += 1 
        return resultado

def iniciar_sesion(usuario, clave):
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql ="SELECT * FROM Usuarios WHERE usuario = ? AND pass = ?;"
        cursor.execute(sql, (usuario, clave))
        resultado = cursor.fetchone()
        return resultado

def mostrar_informe():
    print("***   MOSTRAR INFORME   ***")
    mes = 0
    while True:
        try:
            mes = int(input("Ingrese el mes: "))
            if mes >= 1 and mes <=12:
                break
            else:
                print("El mes ingresado debe ser un número entre 1 y 12")
        except:
            print("El mes ingresado debe ser un número entre 1 y 12")       
    anio = 0
    while True:
        try:
            anio = int(input("Ingrese el año: "))
            fecha_actual = datetime.datetime.now()
            anio_actual = fecha_actual.year
            if anio > 1900 and anio <= anio_actual:
                break
            else:
                print("El año ingresado debe ser un número mayor a 1900 y no mayor al año actual")
        except:
            print("El año ingresado debe ser un número")
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "SELECT SUM(monto) FROM Pagos WHERE mes = ? AND anio = ?;"
        valores = (mes, anio)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()[0]
        print("***********************************************************************")
        print("*                           INFORME MENSUAL                           *")
        print("***********************************************************************")
        print("*                                                                     *")
        if resultado:
            print("*  El dinero recaudado en el mes {:<1} del año {:1} es de: ${:<14}*".format(mes,anio,resultado))
            print("*                                                                     *")
        else:
            print("*  No se encontraron cuotas en el mes {:<1} del año {:<21}*".format(mes,anio))
            print("*                                                                     *")
        print("***********************************************************************")
    except Exception as e:
        print("Error!, no se pudo mostrar el informe{}".format(e))
