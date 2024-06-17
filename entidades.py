import pyodbc
from Conexion import *
from entidades import *

class Socio():
    def __init__(self,id, nombre, rol):
        self.id = id
        self.nombre = nombre
        self.rol = rol
        
class Usuario:
   
    def __init__(self,usuario, password, rol):
        self.usuario = usuario
        self.password = password
        self.rol = rol

    def iniciar_sesion(usuario, clave):
        conn = pyodbc.connect(conexion_sql_server())
        cursor = conn.cursor()
        sql ="select * from Usuarios where Usuario = ? and Pass = ?;"
        cursor.execute(sql, (usuario, clave))
        resultado = cursor.fetchone()
        return resultado

    def alta(nombre):
        try:
            conn = pyodbc.connect(conexion_sql_server())
            cursor = conn.cursor()
            sql = "insert into Clientes (nombre) values (?);"
            valores = (Socio.nombre)
            cursor.execute(sql,valores)
            print(cursor.rowcount,"Registro ingresado")
            conn.close()
        except Exception as e:
            print("Error!, no se pudo dar de alta{}".format(e))

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
            print("Error!, no se pudo dar de alta{}".format(e))

    def modificar():
        while True:
            actualizar = input("\nQuiere actualizar un dato s/n: ")
            if actualizar.lower() == "s":
                try:
                    conn = pyodbc.connect(conexion_sql_server())
                    cursor = conn.cursor()
                    idS = input("Ingrese el ID del socio que desea actualizar: ")
                    sql ="select id from Clientes where Id_cliente = ?;"
                    cursor.execute(sql, idS)
                    resultado = cursor.fetchone()
                    if resultado:
                        nombre = input("Ingrese el nuevo nombre: ")
                        consultaU = "update Clientes set Nombre = ? where Id_cliente = ?;"
                        cursor.execute(consultaU, (nombre, idS))
                        conn.commit()
                    else:
                        print("El ID ingresado es incorrecto!!")
                    conn.close()
                except Exception as e:
                    print("Error!, no se pudo realizar la mofificacion{}".format(e))
            else:
                print("Salio de la opcion modificar")
                break

    def baja():
        while True:
            eliminar = input("\nQuiere eliminar un socio s/n: ")
            if eliminar.lower() == "s":
                try:
                    conn = pyodbc.connect(conexion_sql_server())
                    cursor = conn.cursor()
                    idS = input("Ingrese el ID del socio que desea eliminar: ")
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
            else:
                print("Salio de la opcion Baja")
                break    

    def mostrar_informe():
        pass 
                                 
