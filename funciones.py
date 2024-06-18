import pyodbc
import getpass
import datetime

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
        print("****Login****")
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
        print('1) Registrar pagos')
        print('2) Mostrar comprobante de pago')
        print('3) Alta clientes')
        print('4) Baja clientes')
        print('5) Modificar clientes')
        print('6) Listar clientes')
        print('7) Volver al menu login!')
        opc = input('Elija una opción correcta: ')
        if opc in ['1','2','3','4','5','6','7']:
            return int(opc)

def menu_gestion_gerente():
    print()
    opc = 0
    while True:
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
        opc = input('Elija una opción correcta: ')
        if opc in ['1','2','3','4','5','6','7','8','9']:
            return int(opc)

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
    tipo_de_cuota = ''
    while True:
        tipo_de_cuota = input("Ingrese el tipo de cuota: ")
        if tipo_de_cuota in ['Deportiva', 'Social']:
            break
        else:
            print("El tipo de cuota ingresado debe ser 'Deportiva' o 'Social'")
    id_cliente = int(input("Ingrese el id_cliente: "))
    monto = 0
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sqlId = "SELECT tipo_de_cliente FROM Clientes WHERE id_cliente = ?;"
        cursor.execute(sqlId, id_cliente)
        cliente = cursor.fetchone()[0]
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
                Importe: ${resultado[3]}
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
    print("*** Dar de alta un cliente ***")
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
        consultaV ="SELECT id_cliente from Clientes where id_cliente = ?;"
        cursor.execute(consultaV, idS)
        resultado = cursor.fetchone()
        if resultado:
            consultaD = "UPDATE Clientes SET estado = 'Inactivo' WHERE id_cliente = ?;"
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
            print(f'Cliente: {cliente[0]}, Nombre: {cliente[1]}, Apellido: {cliente[2]}, Teléfono: {cliente[3]}, Deporte: {cliente[4]}, Tipo de cliente: {cliente[5]}, Estado: {cliente[6]}  \n')
        conn.close()
    except Exception as e:
        print("Error!, no se pudo mostrar los clientes{}".format(e))

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
        mes = int(input("Ingrese el mes: "))
        if mes >= 1 and mes <=12:
            break
        else:
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
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "SELECT SUM(monto) FROM Pagos WHERE mes = ? AND anio = ?;"
        valores = (mes, anio)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()[0]
        if resultado:
            print(f'El total de las cuotas del mes {mes} en el año {anio} es de: ${resultado}')
        else:
            print(f"No se encontraron cuotas en el {mes} del año {anio}")
    except Exception as e:
        print("Error!, no se pudo mostrar los clientes{}".format(e))