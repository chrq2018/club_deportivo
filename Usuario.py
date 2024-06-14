from Conexion import *

class Usuario:
    def alta(nombre):
        try:
            conn = Conexion.conexion_sql_server()
            cursor = conn.cursor()
            sql = "insert into socios (nombre) values (?);"
            valores = (nombre)
            cursor.execute(sql,valores)
            print(cursor.rowcount,"Registro ingresado")
            conn.close()
        except Exception as e:
            print("Error!, no se pudo dar de alta{}".format(e))

    def lista():
        try:
            conn = Conexion.conexion_sql_server()
            cursor = conn.cursor()
            sql = "select * from socios;"
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
                    conn = Conexion.conexion_sql_server()
                    cursor = conn.cursor()
                    idS = input("Ingrese el ID del socio que desea actualizar: ")
                    sql ="select id from socios where id = ?;"
                    cursor.execute(sql, idS)
                    resultado = cursor.fetchone()
                    if resultado:
                        nombre = input("Ingrese el nuevo nombre: ")
                        consultaU = "update socios set nombre = ? where id = ?;"
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
                    conn = Conexion.conexion_sql_server()
                    cursor = conn.cursor()
                    idS = input("Ingrese el ID del socio que desea eliminar: ")
                    consultaV ="select id from socios where id = ?;"
                    cursor.execute(consultaV, idS)
                    resultado = cursor.fetchone()
                    if resultado:
                        consultaD = "delete from socios where id = ?;"
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
    