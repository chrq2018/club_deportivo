
# Alta de un Usuario
def alta(nombre, conn):
    with conn.cursor() as cursor:
        consulta = "insert into socios (nombre) values (?);"
        cursor.execute(consulta,(nombre))

def lista(conn):
    with conn.cursor() as cursor:
        consulta = "select * from socios;"
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        while resultado:
            print(resultado)
            resultado = cursor.fetchone()

def modificar(conn):
    while True:
        actualizar = input("\nQuiere actualizar un dato s/n: ")
        if actualizar.lower() == "s":
            with conn.cursor() as cursor:
                idS = input("Ingrese el ID del socio que desea actualizar: ")
                consultaV ="select id from socios where id = ?;"
                cursor.execute(consultaV, idS)
                resultado = cursor.fetchone()
                if resultado:
                    nombre = input("Ingrese el nuevo nombre: ")
                    consultaU = "update socios set nombre = ? where id = ?;"
                    cursor.execute(consultaU, (nombre, idS))
                    conn.commit()
                else:
                    print("El ID ingresado es incorrecto!!")
        else:
            print("Salio de la opcion modificar")
            break

def baja(conn):
    while True:
        eliminar = input("\nQuiere eliminar un socio s/n: ")
        if eliminar.lower() == "s":
            with conn.cursor() as cursor:
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
        else:
            print("Salio de la opcion modificar")
            break

