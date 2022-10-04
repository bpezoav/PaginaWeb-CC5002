#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mysql.connector
import hashlib
import os


class Evento:

    def __init__(self, host, user, password, database):
        # Mantiene la conexion activa
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        # Se encarga de ejecutar las consultas a la DB
        self.cursor = self.db.cursor()

    def save_event(self, data):

        comuna = data[1]

        # Obtener comuna_id
        sqlAux= '''SELECT id FROM comuna c WHERE c.nombre = %s'''
        self.cursor.execute(sqlAux, (comuna,))
        comuna_id = self.cursor.fetchall()[0][0]

        # Insercion en EVENTO

        sql = ''' INSERT INTO evento (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino,
         descripcion, tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) '''
        self.cursor.execute(sql, (comuna_id, *data[2:6], *data[11:15]))
        self.db.commit() # id de la insercion

        # Insercion en RRSS
        id_evento = self.cursor.getlastrowid() # id de la ultima insercion

        sql2= ''' INSERT INTO red_social (nombre, identificador, evento_id) VALUES (%s, %s, %s)'''

        self.cursor.execute(sql2, ('twitter', data[6], id_evento))
        self.db.commit()
        self.cursor.execute(sql2, ('instagram', data[7], id_evento))
        self.db.commit()
        self.cursor.execute(sql2, ('facebook', data[8], id_evento))
        self.db.commit()
        self.cursor.execute(sql2, ('tiktok', data[9], id_evento))
        self.db.commit()
        self.cursor.execute(sql2, ('otra', data[10], id_evento))
        self.db.commit()
        
        # Insercion en FOTO

        l = len(data)
        
        # para evitar las colisiones de archivos
        for i in range(15, l):
            fileitem = data[i]
            filename = fileitem.filename

            sql3 = "SELECT COUNT(id) FROM evento" # total de filas en la base de datos
            self.cursor.execute(sql3) # Realizamos la consulta
            total = self.cursor.fetchall() # Total de elementos en la base // para evitar colisiones del MISMO ARCHIVO
            hash_file = str(total[0][0]) + hashlib.sha256(filename.encode()).hexdigest()[0:30] # total + 30 caracteres de la codificaciona hexadecimal // siempre se guardan asi en la base de datos!

            fn = os.path.basename(filename) # Nombre original del archivo
            open('../media/' + hash_file, 'wb').write(fileitem.file.read()) # lee los bytes del archivo y luego se escriben en el archivo con su hash
            ruta_archivo = "../media/" + hash_file

            sql4 = ''' INSERT INTO foto (ruta_archivo, nombre_archivo, evento_id) VALUES (%s, %s, %s)'''
            self.cursor.execute(sql4, (ruta_archivo, fn, id_evento))
            self.db.commit()


    def get_events(self, tablename):
        # seleccionamos todos los datos de la tabla
        self.cursor.execute(f'SELECT * FROM {tablename}')  # Agregamos el input a la consulta con un f-string
        return self.cursor.fetchall()  # retornamos los datos de la tabla

    def get_lastfiveEvent(self):
        # ultimos 5 eventos
        sql = ''' SELECT id, comuna_id, sector, nombre, email, celular, 
        dia_hora_inicio, dia_hora_termino, descripcion, tipo FROM evento 
        ORDER BY dia_hora_inicio DESC LIMIT 5 '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def obtain_rrss(self, id):
        param = (id, )
        sql = ''' SELECT nombre, identificador FROM red_social WHERE evento_id = %s AND identificador IS NOT NULL'''
        self.cursor.execute(sql, param)
        return self.cursor.fetchall()

    def obtain_photos(self, id):
        param = (id, )
        sql = ''' SELECT ruta_archivo FROM foto WHERE evento_id=%s'''
        self.cursor.execute(sql, param)
        return self.cursor.fetchall()

    def obtener_comunayregionID(self, id):
        param = (id, )
        sql='''SELECT nombre, region_id FROM comuna WHERE id=%s'''
        self.cursor.execute(sql, param)
        return self.cursor.fetchall()

    def obtener_region(self, id):
        param = (id, )
        sql='''SELECT nombre FROM region WHERE id=%s'''
        self.cursor.execute(sql, param)
        return self.cursor.fetchall()

    def obtain_event(self, id):
        param = (id, )
        sql='''SELECT id, comuna_id, sector, nombre, email, celular, 
        dia_hora_inicio, dia_hora_termino, descripcion, tipo FROM evento WHERE id=%s'''
        self.cursor.execute(sql, param)
        return self.cursor.fetchall()

    def events_per_day(self):
        sql ='''SELECT DATE_FORMAT(dia_hora_inicio, '%Y-%m-%d') as fecha,
         count(*) as total from evento group by DATE_FORMAT(dia_hora_inicio, '%Y-%m-%d')
          order by DATE_FORMAT(dia_hora_inicio, '%Y-%m-%d') asc;'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def count_type(self):
        sql = "SELECT tipo as tipocomida, count(*) as total from evento group by tipo order by total asc;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def events_per_hour(self):
        sql1= '''SELECT DATE_FORMAT(dia_hora_inicio, '%Y-%m-%d') as fecha,
        COUNT(CASE WHEN time(dia_hora_inicio) >= '00:00:00' and time(dia_hora_inicio) <= '10:59:59' THEN 1 ELSE NULL END) AS total_manana,
        COUNT(CASE WHEN time(dia_hora_inicio) >= '11:00:00' and time(dia_hora_inicio) <= '14:59:59' THEN 1 ELSE NULL END) AS total_dia, 
        COUNT(CASE WHEN time(dia_hora_inicio) >= '15:00:00' and time(dia_hora_inicio) <= '23:59:59' THEN 1 ELSE NULL END) AS total_tarde
        FROM evento group by DATE_FORMAT(dia_hora_inicio, '%Y-%m-%d');
        '''
        self.cursor.execute(sql1)
        return self.cursor.fetchall()
