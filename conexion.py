
# Coneccion a DB_Club_Deportivo

import pyodbc as odbc
def conexion_sql_server():
    #Datos servidor
    driver = 'SQL SERVER'
    server = 'DESKTOP-7IL9JF9\\SQLEXPRESS'
    database = 'CLUB_DEPORTIVO'
    usuarioDB = 'sa'
    passwordDB = '123'

    cadena_connBD = f"""
        DRIVER={{{driver}}}; 
        SERVER={server}; 
        DATABASE={database};
        Trust_Connection=yes;
        UID={usuarioDB};
        PWD={passwordDB};
    """
    try:
        conexion = odbc.connect(cadena_connBD)
        print("Conexion correcta")
    except Exception as e:
        print("Ocurrio un error al conectar SQL Server: ", e)
    return conexion
    
    



