from myMysql import myMysql

obj=myMysql()
#result=obj.mysqlConnect('localhost','usuario','pass','MiBaseDeDatos')
DB_HOST = '31.170.166.166' 
DB_USER = 'u349685578_admin' 
DB_PASS = '2&JpGfiGN' 
DB_NAME = 'u349685578_clases' 
datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 

result= obj.mysqlConnect(*datos)
if result:

    # ejeplo 1 - INSERT
    obj.prepare("INSERT INTO datos_alumnos VALUES ('juan ', 'salinas', '30')", None, False)
    print(obj.lastId)

    # ejemplo 2 - UPDATE
    query="UPDATE datos_alumnos SET nombre=%s WHERE apellido=%s"
    params=("Juan Miguel","Salinas")
    obj.prepare(query,params,False)
    if result:
        print(result)
    else:
        print(obj.error)
    print(obj.affectedRows())

    # ejemplo 3 - SELECT
    result=obj.prepare("SELECT * FROM datos_alumnos ")
    print(result)
    if result:
        print(result)
    else:
        print(obj.error)

    obj.mysqlClose()
else:
    print(obj.error)