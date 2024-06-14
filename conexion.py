
# Coneccion a DB_Club_Deportivo

import pyodbc as odbc

class Conexion:

    def conexion_sql_server():
        
        try:
        #Datos servidor
            driver = 'SQL SERVER'
            server = 'DESKTOP-7IL9JF9\\SQLEXPRESS'
            database = 'CLUB_DEPORTIVO'
            usuarioDB = 'sa'
            passwordDB = '123'

            conexion = odbc.connect(
                 'DRIVER='+driver+'; SERVER='+server+';DATABASE='+database+
                 ';Trust_Connection=yes;UID='+usuarioDB+';PWD='+passwordDB
                )
            #print("Conexion exitosa!")
        except ConnectionError as e:
                print("Ocurrio un error al conectar SQL Server: ", e)
        return conexion
    
    



