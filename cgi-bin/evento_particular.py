#!/usr/bin/python3
# -*- coding: utf-8 -*-

import db
import cgi
import cgitb
import html

# Creamos un formulario para poder mostrar los datos del evento en particular

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

cgitb.enable()

# Abrimos una conexion a la base de datos
Eventdb = db.Evento("localhost", "cc500209_u", "usvestibul", "cc500209_db")

header= '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Tarea 3</title>
    <link rel="stylesheet" href="../../Tarea3/estilos.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
'''
print(header, file=utf8stdout)
form = '''
<body>
<div class="main">
    <form action="evento_particular.py" method="get" class="oculto">
        <input id="ident" name="ident" class="oculto">
    </form>
'''

form = cgi.FieldStorage()

i=0
if "ident" in form:
    idt = html.escape(form["ident"].value, quote=True)
    evento = Eventdb.obtain_event(idt) # lista con la tupla con todos los valores del evento
    fotos = Eventdb.obtain_photos(idt)
    comuna = Eventdb.obtener_comunayregionID(evento[0][1])[0][0]
    regionid = Eventdb.obtener_comunayregionID(evento[0][1])[0][1]
    region = Eventdb.obtener_region(regionid)[0][0]
    rrss = Eventdb.obtain_rrss(idt)
    if len(str(evento[0][2])) == 0:
        sector = "<p> No hay información </p>"
    else:
        sector = evento[0][2]
    if len(str(evento[0][8])) == 0:
        desc = "<p> No hay información </p>"
    else:
        desc = evento[0][8]

consulta = f'''
    <p class="negrita"> Información sobre el evento: </p>
        <table class="table">
            <tr>
                <th>Fecha - hora inicio
                <th>Región
                <th>Comuna
                <th>Sector
                <th>Tipo comida
                <th>Descripción
                <th>Nombre contacto
                <th>Número contacto
                <th>E-mail contacto
                <th>Redes sociales
                <th>Total fotos
            </tr>
            <tr>
                <td>{str(evento[0][6])}</td> 
                <td>{str(evento[0][7])}</td>
                <td>{str(region)}</td>
                <td>{str(comuna)}</td>
                <td>{sector}</td>
                <td>{str(evento[0][9])}</td>
                <td>{desc}</td>
                <td>{str(evento[0][3])}</td>
                <td>{str(evento[0][5])}</td>
                <td>{str(evento[0][4])}</td>
'''
print(consulta, file=utf8stdout)
print("             <td>", file=utf8stdout)

if len(rrss) == 0:
    print("<p> No hay información </p>", file=utf8stdout)
    print("             </td>", file=utf8stdout)
else:
    for r in rrss:
        print("<p> " + str(r[0]) + ": " + str(r[1]) + "</p>", file=utf8stdout)
    print("             </td>", file=utf8stdout)
    print("             <td>", file=utf8stdout)
for f in fotos:
    i_d = "img" + str(i)
    print("<img id='" + i_d + "' src='../" + f[0] + "' height='320' width='240' " + "onclick=" + "(agrandarImagen(" + i_d + ")) alt=''>", file=utf8stdout)
    print("<button onclick=" + "(resetImagen(" + i_d + "))>&times;</button>", file=utf8stdout)
    i +=1
print("             </td>", file=utf8stdout)
print("         </tr>", file=utf8stdout)

bottom = '''
    </table>
    <br>
    <div>
        <button class="volver" onclick="window.location='index.py'">Volver a la portada</button> 
        <button class="volver" onclick="window.location='mostrar_listado.py'">Volver al listado de eventos</button>
    </div>
</div>

<script src="../../Tarea3/scriptTarea.js"></script>

</body>

</html>
'''
print(bottom, file=utf8stdout)
 
