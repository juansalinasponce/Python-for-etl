#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import MySQLdb
 
class myMysql(object):
 
    def __init__(self):
        # Variable que determina si estamos conectados a MySQL...
        self.connected=0
        self.error=""
 
    def mysqlConnect(self,host,user,pw,database,port=3306):
        """
        Realiza la conexion con la base de datos
        Tiene que recibir:
            - host
            - user
            - pw => password
            - database => database name
        Puede recibir:
            - port
        Devuelve True o False
        """
        try:
            self.db = MySQLdb.connect(user=user, passwd=pw, host=host, db=database, port=port, charset="utf8", init_command="set names utf8")
            self.cursor = self.db.cursor()
            self.connected=1
            return True
        except:
            self.error="Error desconocido"
        return False
 
    def prepare(self,query,params=None,execute=True):
        """
        Funcion que ejecuta una instruccion mysql
        Tiene que recibir:
            - query
        Puede recibir:
            - params => tupla con las variables
            - execute => devuelve los registros
        Devuelve False en caso de error
        """
        if self.connected:
            self.error=""

            self.cursor.execute(query,params)
            self.db.commit()
            if execute:
                # convert de result to dictionary
                result = []
                columns = tuple([d[0].encode().decode('utf8') for d in self.cursor.description])
                for row in self.cursor:
                    result.append(dict(zip(columns, row)))
                return result
            return True
        return False
 
    def lastId(self):
        """
        Funcion que devuelve el ultimo id añadido
        """
        return self.cursor.lastrowid
 
    def affectedRows(self):
        return self.cursor.rowcount
 
    def mysqlClose(self):
        """
        Funcion para cerrar la conexion con la base de datos
        """
        self.connected=0
        try:
            self.cursor.close()
        except:pass
        try:
            self.cnx.close()
        except:pass
 
    def fetchOneAssoc(self,cursor) :
        data = cursor.fetchone()
        if data == None :
            return None
        desc = cursor.description
 
        dict = {}
 
        for (name, value) in zip(desc, data) :
            dict[name[0]] = value
 
        return dict
 