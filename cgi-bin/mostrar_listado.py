#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import db
import mysql.connector

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

cgitb.enable()


# Abrimos una conexion a la base de datos
Eventdb = db.Evento("localhost", "cc500209_u", "usvestibul", "cc500209_db")

# creo una variable que contiene la informacion de la tabla de la base de datos
events = Eventdb.get_events('evento')

if len(events)>0:

    header = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Tarea 3</title>
        <link rel="stylesheet" href="../../Tarea3/estilos.css">
        <link rel="stylesheet" href="../../Tarea3/paginate.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script type="text/javascript" src="../../Tarea3/paginate.js"></script>

    </head>
    '''

    b1 = '''
    <body>

    <div class="main">

        <ul class="topnav">
            <li><a href="index.py">Portada</a></li>
            <li><a href="../../Tarea3/form.html">Informar un evento</a></li>
            <li><a href="mostrar_listado.py">Ver listado de eventos</a></li>
            <li><a href="../../Tarea3/estadisticas.html">Estadísticas</a></li>
        </ul>

        <div class="negrita" id="listado-de-eventos"> <h1>Lista de eventos</h1> </div>
        <p style="text-align: center"> Haga click sobre la fila para obtener mas información sobre el evento.</p>
            <table class="table content" id="paginacion">
                <thead>
                    <tr>
                        <th>Fecha - hora inicio
                        <th>Fecha - hora termino
                        <th>Comuna
                        <th>Sector
                        <th>Tipo comida
                        <th>Nombre contacto
                        <th>Total fotos
                    </tr>
                </thead>
                <tbody>
    '''
    print(header, file=utf8stdout)
    print(b1, file=utf8stdout)

    i=0
    for e in events:
        rrss = Eventdb.obtain_rrss(e[0]) # lista con las tuplas [(nombre, identificador), (...), ...] donde si hay identificador
        fotos = Eventdb.obtain_photos(e[0]) # lista con las fotos ((ruta1), (ruta2), (ruta3), (ruta4))
        comuna = Eventdb.obtener_comunayregionID(e[1])[0][0] # lista con la tupla (comuna, region_id)
        regionid = Eventdb.obtener_comunayregionID(e[1])[0][1]
        region = Eventdb.obtener_region(regionid)[0][0]
        if len(str(e[2])) == 0:
            sector = "<p> No hay información </p>"
        else:
            sector = e[2]

        row = f'''
                <tr onclick="moreInfo({str(e[0])})">
                    <td>{str(e[6])}</td> 
                    <td>{str(e[7])}</td>
                    <td>{str(comuna)}</td>
                    <td>{sector}</td>
                    <td>{str(e[9])}</td>
                    <td>{str(e[3])}</td>
        '''
        print(row, file=utf8stdout)
        
        print("                    <td>", file=utf8stdout)
        for f in fotos:
            i_d = "img" + str(i)
            print("<img id='" + i_d + "' src='../" + f[0] + "' height='320' width='240' " + "onclick=" + "(agrandarImagen(" + i_d + ")) alt=''>", file=utf8stdout)
            print("<button onclick=" + "(resetImagen('" + i_d + "'))>&times;</button>", file=utf8stdout)
            i +=1
        print("                    </td>", file=utf8stdout)
        print("                    </tr>", file=utf8stdout)


    bottom = '''
                </tbody>
            </table>
            <br>
        <div id="buttons" class="paginate paginate_controls">
        </div>
        <script> 
            let options = {
                numberPerPage:5, 
                pageCounter:true
            };
            paginate.init('.content', options);
        </script>
    </div>

    <script src="../../Tarea3/scriptTarea.js"></script>
    

    </body>

    </html>
    '''
    print(bottom, file=utf8stdout)

else:
    head = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Tarea 2</title>
        <link rel="stylesheet" href="../../Tarea3/estilos.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    </head> 
    '''

    b1 = '''
        <body>

        <div class=main>
            <ul class="topnav">
                <li><a href="../../Tarea3/index.html">Portada</a></li>
                <li><a href="../../Tarea3/form.html">Informar un evento</a></li>
                <li><a href="mostrar_listado.py">Ver listado de eventos</a></button>
                <li><a href="../../Tarea3/estadisticas.html">Estadísticas</a></li>  
            </ul>
            <p class="negrita centrada"> A&uacute;n no hay información en la base de datos </p>
        '''
    b2 = '''
    </div>

    </body>

    </html>
    '''
    print(head, file=utf8stdout)
    print(b1, file=utf8stdout)
    print(b2, file=utf8stdout)