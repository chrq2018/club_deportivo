import pyodbc
import getpass

def conexion_sql_server():
    try:
        conexion = 'DRIVER={SQL SERVER}; SERVER=MARIANA\SQLEXPRESS;DATABASE=CLUB_DEPORTIVO;Trust_Connection={yes}; UID=sa; PWD=123'                    
    except ConnectionError as e:
                print("Ocurrio un error al conectar SQL Server: ", e)
    return conexion

def menu_login():
    print()
    opc = 0
    while opc < 1 or opc > 2:
        print("****Login****")
        print('1) Inicio')
        print('2) Salir')
        opc = int(input('Elija una opción correcta: '))
    return opc

def menu_gestion_empleado():
    print()
    opc = 0
    while opc < 1 or opc > 8:
        print()
        print('1) Registrar pagos')
        print('2) Mostrar comprobante de pago')
        print('3) Alta clientes')
        print('4) Baja clientes')
        print('5) Modificar clientes')
        print('6) Listar clientes')
        print('7) Volver al menu login!')
        opc = int(input('Elija una opción correcta: '))
    return opc

def menu_gestion_gerente():
    print()
    opc = 0
    while opc < 1 or opc > 10:
        print()
        print('1) Registrar pagos')
        print('2) Mostrar comprobante de pago')
        print('3) Mostrar pagos')
        print('4) Alta clientes')
        print('5) Baja clientes')
        print('6) Modificar clientes')
        print('7) Listar clientes')
        print('8) Imprimir Informes')
        print('9) Volver al menu login!')
        opc = int(input('Elija una opción correcta: '))
    return opc
        
def registrar_pago():
    print("***Registrar pagos***\n")
    mes = 0
    while True:
        mes = int(input("Ingrese el mes: "))
        if mes >= 1 and mes <=12:
            break
        else:
            print("El mes ingresado debe estar entre 1 y 12")
    anio = int(input("Ingrese el año: "))
    monto = float(input("Ingrese el monto: "))
    tipo_de_cuota = ''
    while True:
        tipo_de_cuota = input("Ingrese el tipo de cuota: ")
        if tipo_de_cuota in ['Deportiva', 'Social']:
            break
        else:
            print("El tipo de cuota ingresado debe ser 'Deportiva' o 'Social'")
    id_cliente = int(input("Ingrese el id_cliente: "))
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "INSERT INTO Pagos (mes, anio, monto, tipo_de_cuota, id_cliente) values (?, ?, ?, ?, ?);"
        valores = (mes, anio, monto, tipo_de_cuota, id_cliente)
        cursor.execute(sql,valores)
        conn.commit()
        print(cursor.rowcount,"Registro ingresado") 
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
            print("*** Comprobante de pago***")
            print(f"""
                Cliente: {resultado[5]}
                Cuota: {resultado[4]}
                Mes: {resultado[1]}
                Año: {resultado[2]}
                Importe: ${round(resultado[3],2)}
                """)
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
        for pago in resultado:
            print(f'Pago: {pago[0]}, Mes: {pago[1]}, Año: {pago[2]}, Monto: {pago[3]}, Tipo de cuota: {pago[4]}, Cliente: {pago[5]} \n')
        conn.close()
    except Exception as e:
        print("Error!, no se puden mostrar los pagos {}".format(e))



def alta():
    print("***Dar de alta un cliente***")
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
        sql = "SELECT * FROM Clientes;"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        for cliente in resultado:
            print(f'id cliente: {cliente[0]}, {cliente[1]} {cliente[2]}\n')
        idS = input("Ingrese el ID del cliente que desea eliminar: ")
        consultaV ="SELECT id_cliente from Clientes where id_cliente = ?;"
        cursor.execute(consultaV, idS)
        resultado = cursor.fetchone()
        if resultado:
            consultaD = "UPDATE Clientes SET estado = Inactivo WHERE id_cliente = ?;"
            cursor.execute(consultaD, (idS))
            conn.commit()
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
                if deporte in ['Fútbol', 'Básquet', 'Tenis']:
                    sql = "UPDATE Clientes SET deporte = ? where id_cliente = ?;"
                    cursor.execute(sql, (deporte, idS))
                    conn.commit()
                    break
                else:
                    print("El deporte ingresado debe ser 'Fútbol', 'Básquet' o 'Tenis'")
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
        for cliente in resultado:
            print(f'Cliente: {cliente[0]}, Nombre: {cliente[1]}, Apellido: {cliente[2]}, Teléfono: {cliente[3]}, Deporte: {cliente[4]}, Tipo de cliente: {cliente[5]} \n')
        conn.close()
    except Exception as e:
        print("Error!, no se pudo mostrar los socios{}".format(e))

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
        sql ="SELECT * FROM Usuarios where usuario = ? and pass = ?;"
        cursor.execute(sql, (usuario, clave))
        resultado = cursor.fetchone()
        return resultado

def mostrar_informe():
    pass 
                                 
