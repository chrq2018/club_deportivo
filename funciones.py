import pyodbc
import getpass

def conexion_sql_server():
    try:
        conexion = 'DRIVER={SQL SERVER}; SERVER=DESKTOP-7IL9JF9\\SQLEXPRESS;DATABASE=CLUB_DEPORTIVO;Trust_Connection={yes}; UID=sa; PWD=123'                    
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
    while opc < 1 or opc > 7:
        print()
        print('1) Registrar pagos')
        print('2) Alta clientes')
        print('3) Baja clientes')
        print('4) Modificar clientes')
        print('5) Listar clientes')
        print('6) Volver al menu login!')
        opc = int(input('Elija una opción correcta: '))
    return opc

def menu_gestion_gerente():
    print()
    opc = 0
    while opc < 1 or opc > 8:
        print()
        print('1) Registrar pagos')
        print('2) Mostrar pagos')
        print('3) Alta clientes')
        print('4) Baja clientes')
        print('5) Modificar clientes')
        print('6) Listar clientes')
        print('7) Imprimir Informes')
        print('8) Volver al menu login!')
        opc = int(input('Elija una opción correcta: '))
    return opc
        
def registrar_pagos(mes, anio, monto, tipo_de_cuota, id_cliente):
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "insert into Pagos (Mes, Anio, Monto, Tipo_de_cuota, Id_cliente) values (?, ?, ?, ?, ?);"
        valores = (mes, anio, monto, tipo_de_cuota, id_cliente)
        cursor.execute(sql,valores)
        conn.commit()
        print(cursor.rowcount,"Registro ingresado")
        conn.close()
    except Exception as e:
        print("Error!, no se pudo registrar el pago{}".format(e))

def mostrar_pagos():
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "select * from Pagos;"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        while resultado:
            print(resultado)
            resultado = cursor.fetchone()
        conn.close()
    except Exception as e:
        print("Error!, no se pudo mostrar los pagos {}".format(e))

def alta(nombre, apellido, telefono, deporte, tipo_de_cliente):
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "insert into Clientes (Nombre, Apellido, Telefono, Deporte, Tipo_de_cliente) values (?, ?, ?, ?, ?);"
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
        idS = input("Ingrese el ID del cliente que desea eliminar: ")
        consultaV ="select Id_cliente from Clientes where id_cliente = ?;"
        cursor.execute(consultaV, idS)
        resultado = cursor.fetchone()
        if resultado:
            consultaD = "delete from Clientes where id_cliente = ?;"
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
        idS = input("Ingrese el ID del socio que desea actualizar: ")
        sql ="select id_cliente from Clientes where Id_cliente = ?;"
        cursor.execute(sql, idS)
        resultado = cursor.fetchone()
        if resultado:
            deporte = input("Ingrese el nuevo deporte: ")
            sql = "update Clientes set deporte = ? where Id_cliente = ?;"
            cursor.execute(sql, (deporte, idS))
            conn.commit()
        else:
            print("El ID ingresado es incorrecto!!")
        conn.close()
    except Exception as e:
        print("Error!, no se pudo realizar la mofificacion{}".format(e))

def lista():
    try:
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql = "select * from Clientes;"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        while resultado:
            print(resultado)
            resultado = cursor.fetchone()
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
                print("Ingreso correcto")
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
        sql ="select * from Usuarios where Usuario = ? and Pass = ?;"
        cursor.execute(sql, (usuario, clave))
        resultado = cursor.fetchone()
        return resultado

def mostrar_informe():
    pass 
                                 
