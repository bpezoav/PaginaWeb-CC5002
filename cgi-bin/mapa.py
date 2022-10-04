#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json, db, cgitb
from difflib import SequenceMatcher

cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')


Eventdb = db.Evento("localhost", "cc500209_u", "usvestibul", "cc500209_db")

events = Eventdb.get_events('evento')

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


with open('../../Tarea3/geoChile.json') as fp:
    geo = json.load(fp)

data = []

for e in events:
    row = []
    ident = e[0]
    dia_inicio = e[6].strftime('%Y-%m-%d')
    tipo = e[9]
    sector = e[2]
    fotos = Eventdb.obtain_photos(e[0]) # lista con las fotos ((ruta1), (ruta2), (ruta3), (ruta4))
    comuna = Eventdb.obtener_comunayregionID(e[1])[0][0] # lista con la tupla (comuna, region_id)
    row.append(dia_inicio)
    row.append(tipo)
    row.append(sector)
    row.append(fotos)  # => row = ["fecha inicio", "tipo", "sector", [(ruta1), (ruta2), ...]]
    for i in geo:
        if similar(i['name'], comuna) >=0.8:
            a = (i['lat'], i['lng'])
            row.append(a) # agregamos a data la tupla (lat, long) => row = ["fecha inicio", "tipo", "sector", [(ruta1), (ruta2), ...], (lat,long)]
    row.append(ident)
    data.append(row)

# => row[0] = fecha, row[1] = tipo, row[2]=sector, row[3][i] = ruta i, row[4][0] = latitud, row[4][1] = longt, row[5] = id
print(json.dumps(data))