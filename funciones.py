import pyodbc
import getpass
import datetime
from os import system

def conexion_sql_server():
    try:
        conexion = 'DRIVER={SQL SERVER}; SERVER=DESKTOP-32A2485\SQLEXPRESS;DATABASE=CLUB_DEPORTIVO;Trust_Connection={yes}; UID=sa; PWD=123'                    
    except ConnectionError as e:
                print("Ocurrio un error al conectar SQL Server: ", e)
    return conexion

def menu_login():
    print()
    opc = 0
    while True:
        print("***************************")
        print("*          LOGIN         *")
        print("***************************")
        print()
        print('1) Inicio')
        print('2) Salir')
        opc = input('Elija una opción correcta: ')
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
            resultado = validar_inicio_sesion()
            rol = resultado[3]
        elif op2 == 2:
            alta()
        elif op2 == 3:
            print("***Dar de baja un cliente***")
            while True:
                eliminar = input("\nQuiere eliminar un cliente s/n: ")
                if eliminar.lower() == "s":
                    baja()
                    break
                else:
                    print("Salio de la opcion Baja")
                    break    
        elif op2 == 4:
            print("Modificar los datos de un cliente")
            while True:
                actualizar = input("\nQuiere actualizar un dato s/n: ")
                if actualizar.lower() == "s":
                    modificar()
                else:
                    print("Salio de la opcion modificar")
                    break
        elif op2 == 5:
            ver_cliente()
        elif op2 == 6:
            print("***Lista de clientes***\n")
            lista() 
        elif op2 ==7:
             registrar_pago()
        elif op2 ==8:
            id_cliente = int(input("Ingrese el id_cliente: "))
            mes = int(input("Ingrese el mes: "))
            mostrar_comprobante_pago(id_cliente, mes)
        
def input_validado(mensaje):
    valor = ''
    while True:
        valor = input(mensaje)
        if valor != '':
            return valor
        
def registrar_pago():
    print("***Registrar pagos***\n")
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
    id_cliente = int(input("Ingrese el id_cliente: "))
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
        if deporte != 'NULL':
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
            print("|Cliente:     {:<15}|".format(resultado[0]))
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
        print("Listado de todos los pagos:\n")
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
    print("*** Dar de alta un cliente ***")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = input("Ingrese el telefono: ")
    deporte = ''
    while True:
        deporte = input("Ingrese el nuevo deporte: ")
        if deporte in ['Fútbol', 'Básquet', 'Tenis', 'NULL']:
            break
        else:
            print("El deporte ingresado debe ser 'Fútbol', 'Básquet', 'Tenis' o 'NULL'")
    tipo_de_cliente = ''
    while True:
        tipo_de_cliente = input("Ingrese el tipo de cliente: ")
        if tipo_de_cliente in ['Socio', 'No socio', 'Invitado']:
            break
        else:
            print("El tipo de cliente ingresado debe ser 'Socio', 'No socio' o 'Invitado'")
    estado = 'Activo'
    if tipo_de_cliente == 'Invitado':
        estado = 'NULL'
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "INSERT INTO Clientes (nombre, apellido, telefono, deporte, tipo_de_cliente, estado) values (?, ?, ?, ?, ?, ?);"
        valores = (nombre, apellido, telefono, deporte, tipo_de_cliente, estado)
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
        sql = "SELECT * FROM Clientes;"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        for cliente in resultado:
            print(f'id cliente: {cliente[0]}, {cliente[1]} {cliente[2]}\n')
        idS = input("Ingrese el ID del cliente que desea eliminar: ")
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
        for cliente in resultado:
            print(f'id cliente: {cliente[0]}, {cliente[1]} {cliente[2]}, deporte: {cliente[4]}\n')
        idS = input("Ingrese el ID del cliente que desea actualizar: ")
        sql ="SELECT id_cliente from Clientes where id_cliente = ?;"
        cursor.execute(sql, idS)
        resultado = cursor.fetchone()
        if resultado:
            while True:
                deporte = input("Ingrese el nuevo deporte: ")
                if deporte in ['Fútbol', 'Básquet', 'Tenis', 'NULL']:
                    sql = "UPDATE Clientes SET deporte = ? where id_cliente = ?;"
                    cursor.execute(sql, (deporte, idS))
                    conn.commit()
                    break
                else:
                    print("El deporte ingresado debe ser 'Fútbol', 'Básquet', 'Tenis' o 'NULL'")
        else:
                print("El ID ingresado es incorrecto!!")
        conn.close()
    except Exception as e:
        print("Error!, no se pudo realizar la mofificacion{}".format(e))

def lista():
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
           
            print("|{:^8}|{:^16}|{:^15}|{:^13}|{:^12}|{:^18}|{:^10}|".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4],cliente[5],cliente[6]))
        print("----------------------------------------------------------------------------------------------------")
        conn.close()
    except Exception as e:
        print("Error!, no se pudo mostrar los clientes{}".format(e))

def ver_cliente():
    try:
        idS = input("\nIngrese el apellido o nombre del cliente que desea buscar: ")
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "SELECT * FROM Clientes WHERE apellido LIKE ? OR nombre LIKE ?;"
        cursor.execute(sql, ('%' + idS + '%', '%' + idS + '%'))
        resultado = cursor.fetchall()
        if resultado:
            for cliente in resultado:
                print(f'\nCliente: {cliente[0]}, Nombre: {cliente[1]}, Apellido: {cliente[2]}, Teléfono: {cliente[3]}, Deporte: {cliente[4]}, Tipo de cliente: {cliente[5]}, Estado: {cliente[6]}  \n')
        else:
            print(f"No se ha encontrado al cliente: {idS}")
        conn.close()
    except Exception as e:
        print("Error!, no se pudo mostrar a los clientes{}".format(e))


def validar_inicio_sesion():
        cont = 1
        while cont <= 3:   
            usuario = input("Ingrese usuario: ")
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
    mes = 0
    while True:
        try:
            mes = int(input("Ingrese el mes: "))
            if mes >= 1 and mes <=12:
                break
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
        if resultado:
            print(f'El dinero recaudado en el mes {mes} del año {anio} es de: ${resultado}')
        else:
            print(f"No se encontraron cuotas en el {mes} del año {anio}")
    except Exception as e:
        print("Error!, no se pudo mostrar el informe{}".format(e))
