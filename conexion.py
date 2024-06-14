
def conexion_sql_server():
        
    try:
        conexion = 'DRIVER={SQL SERVER}; SERVER=DESKTOP-7IL9JF9\\SQLEXPRESS;DATABASE=CLUB_DEPORTIVO;Trust_Connection={yes}; UID=sa; PWD=123'                    
    except ConnectionError as e:
                print("Ocurrio un error al conectar SQL Server: ", e)
    return conexion
    
    



