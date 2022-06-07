import requests
import json
from myMysql import myMysql

resp = requests.get('http://ip-api.com/json/208.80.152.201')
data_api = json.loads(resp.content)
print(data_api)
print(data_api['status'])

obj=myMysql()

#result=obj.mysqlConnect('localhost','usuario','pass','MiBaseDeDatos')
DB_HOST = '31.170.166.166' 
DB_USER = 'u349685578_admin' 
DB_PASS = '2&JpGfiGN' 
DB_NAME = 'u349685578_clases' 
datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 

result= obj.mysqlConnect(*datos)
if result:
    column= "status,country,countryCode,region,regionName,city"
    query = "INSERT INTO tabla_api({0}) VALUES ('{1}','{2}','{3}','{4}','{5}','{6}')".format(column,data_api['status'],
                                                                                 data_api['country'],data_api['countryCode'],
                                                                                 data_api['region'],data_api['regionName'],
                                                                                 data_api['city'])
    print(query)
    obj.prepare(query, None, False)
    print("Se guardó en base de datos")