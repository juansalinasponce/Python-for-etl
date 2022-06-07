import MySQLdb

DB_HOST = '31.170.166.166' 
DB_USER = 'u349685578_admin' 
DB_PASS = '2&JpGfiGN' 
DB_NAME = 'u349685578_clases'

def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
    
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 

    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
    
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 

    return data

query_personalizado = 'Select * from datos_alumnos'
result = run_query(query_personalizado)
print(result)