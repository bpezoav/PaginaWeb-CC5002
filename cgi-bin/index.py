#!/usr/bin/python3
# -*- coding: utf-8 -*-

import db
import cgitb
import cgi

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

cgitb.enable()

# Abrimos una conexion a la base de datos
Eventdb = db.Evento("localhost", "cc500209_u", "usvestibul", "cc500209_db")

# ultimos eventos
eventos = Eventdb.get_lastfiveEvent()

header = '''
<!-- HTML5 -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Tarea 3</title>
    <link rel="stylesheet" href="../../Tarea3/estilos.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
</head>
'''
print(header, file=utf8stdout)

body = '''
<body>

<div class="titulo negrita" id="portada">Bienvenidx!!</div>

<div class="main">
        
    <ul class="topnav">
        <li><a href="index.py">Portada</a></li>
        <li><a href="../../Tarea3/form.html">Informar un evento</a></li>
        <li><a href="mostrar_listado.py">Ver listado de eventos</a></button>
        <li><a href="../../Tarea3/estadisticas.html">Estadísticas</a></li>  
    </ul>

    <br>
    <br>

    <div class="negrita">Últimos cinco eventos listados:</div>

    <br>

    <table class="table">

        <tr>
            <th>Fecha - hora inicio
            <th>Fecha - hora termino
            <th>Comuna
            <th>Sector
            <th>Tipo
            <th>Foto
        </tr>
'''
print(body, file=utf8stdout)

for e in eventos:
    fotos = Eventdb.obtain_photos(e[0])
    comuna = Eventdb.obtener_comunayregionID(e[1])[0][0]
    if len(str(e[2])) == 0:
        sector = "<p> No hay información </p>"
    else:
        sector = e[2]
    row = f'''
        <tr>
            <td>{str(e[6])}
            <td>{str(e[7])}
            <td>{str(comuna)}
            <td>{sector}
            <td>{str(e[9])}
            <td><img src="../{str(fotos[0][0])}" width="140" height="100" alt="">
        </tr>
    '''
    print(row, file=utf8stdout)

mapa = '''
    </table>
    <h1> Mapa de eventos</h1>
    <div id='map'>
        <script src="../../Tarea3/map.js"></script>
    </div>

'''
print(mapa, file=utf8stdout)

bottom = '''
</div>
<script src="../../Tarea3/scriptTarea.js"></script>
</body>

</html>
'''
print(bottom, file=utf8stdout)