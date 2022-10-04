#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi, json, db, cgitb, datetime

cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

form = cgi.FieldStorage()
# print(form, "\n")

if 'tipo' in form:
    

    tipo = form.getvalue('tipo')

    # Abrimos una conexion a la base de datos

    Eventdb = db.Evento("localhost", "cc500209_u", "usvestibul", "cc500209_db")

    if tipo == 'eventosxdia':
        data = Eventdb.events_per_day() # obtenemos la informacion de la consulta

    elif tipo == 'torta':
        data = Eventdb.count_type()

    elif tipo == 'barras':
        data = Eventdb.events_per_hour()

    rows = {}
    k=0
    for d in data:
        rows[k] = list(d) # diccionario con listas como valores
        k+=1

    print(json.dumps(rows)) # devolvemos como un archivo json

else:
    print("Error con el formulario \n")