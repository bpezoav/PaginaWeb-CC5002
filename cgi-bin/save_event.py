#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cgi
import cgitb
import db
import filetype
import os
import re
from datetime import datetime
import html

cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage() # Accedemos a los datos del formulario

# Verificacion de los inputs

Error = "" # Mensaje de error a mostrar

# Region y comuna

regiones = ['Región Arica y Parinacota', 'Región de Tarapacá', 'Región de Antofagasta',
    'Región de Atacama', 'Región de Coquimbo', 'Región de Valparaiso', 'Región Metropolitana de Santiago',
    'Región del Libertador General Bernardo Ohiggins', 'Región del Maule', 'Región del Ñuble',
    'Región del Biobío', 'Región de La Araucanía', 'Región de Los Ríos', 'Región de Los Lagos',
    'Región Aisén del General Carlos Ibáñez del Campo', 'Región de Magallanes y la Antártica Chilena']

dict_comunas = {'Región Arica y Parinacota': ['Arica', 'Camarones', 'Gral. Lagos', 'Putre'],
    'Región de Tarapacá': ['Alto Hospicio', 'Iquique', 'Camiña', 'Colchane', 'Huara', 'Pica', 'Pozo Almonte'],
    'Región de Antofagasta': ['Antofagasta', 'Mejillones', 'Sierra Gorda', 'Taltal', 'Calama', 'Ollague', 'San Pedro Atacama', 'Maria Elena', 'Tocopilla'],
    'Región de Atacama': ['Chañaral', 'Diego de Almagro', 'Caldera', 'Copiapó', 'Tierra Amarilla', 'Alto del Carmen', 'Freirina', 'Huasco', 'Vallenar'],
    'Región de Coquimbo': ['Canela', 'Illapel', 'Los Vilos', 'Salamanca', 'Andacollo', 'Coquimbo', 'La Higuera', 'La Serena', 'Paihuano', 'Vicuña', 'Combarbala', 'Monte Patria', 'Ovalle', 'Punitaqui', 'Rio Hurtado'],
    'Región de Valparaiso': ['Isla de pascua', 'Calle Larga', 'Los Andres', 'Rinconada de Los Andes', 'San Esteban', 'Limache', 'Olmue', 'Quilpue', 'Villa Alemana', 'Cabildo', 'La Ligua', 'Papudo', 'Petorca', 'Zapallar', 'Hijuela', 'La Calera', 'La Cruz', 'Nogales', 'Quillota', 'Algarrobo', 'Cartagena', 'El Quisco', 'El Tabo', 'San Antonio', 'Santo Domingo', 'Catemu', 'Llay Llay', 'Panquehue', 'Putaendo', 'San Felipe', 'Santa María', 'Casablanca', 'Concon', 'Juan Fernandez', 'Puchuncavi', 'Quintero', 'Valparaiso', 'Viña del Mar'],
    'Región Metropolitana de Santiago': ['Colina', 'Lampa', 'Tiltil', 'Pirque', 'Puente Alto', 'San Jose de Maipo', 'Buin', 'Calera de Tango', 'Paine', 'San Bernardo', 'Alhue', 'Curacavi', 'Maria Pinto', 'Melipilla', 'San Pedro', 'Cerrillos', 'Cerro Navia', 'Conchali', 'El Bosque', 'Estacion Central', 'Huechuraba', 'Independencia', 'La Cisterna', 'La Granja', 'La Florida', 'La Pintana', 'La Reina', 'Las Condes', 'Lo Barnechea', 'Lo Espejo', 'Lo Prado', 'Macul', 'Maipu', 'Ñuñoa', 'Pedro Aguirre Cerda', 'Peñalolen', 'Providencia', 'Pudahuel', 'Quilicura', 'Quinta Normal', 'Recoleta', 'Renca', 'San Miguel', 'San Joaquin', 'San Ramon', 'Santiago', 'Vitacura', 'El Monte', 'Isla de Maipo', 'Padre Hurtado', 'Peñaflor', 'Talagante'],
    'Región del Libertador General Bernardo Ohiggins': ['Codegua', 'Coinco', 'Coltauco', 'Doñihue', 'Graneros', 'Las Cabras', 'Machali', 'Malloa', 'Olivar', 'Peumo', 'Pichidegua', 'Quinta Tilcoco', 'Rancagua', 'Requinoa', 'Rengo', 'Mostazal', 'San Vicente', 'La Estrella', 'Litueche', 'Marchigue', 'Navidad', 'Paredones', 'Pichilemu', 'Chepica', 'Chimbarongo', 'Lolol', 'Nancagua', 'Palmilla', 'Peralillo', 'Placilla', 'Pumanque', 'San Fernando', 'Santa Cruz'],
    'Región del Maule': ['Curico', 'Hualañe', 'Licanten', 'Molina', 'Rauco', 'Romeral', 'Sagrada Familia', 'Teno', 'Vichuquen', 'Colbun', 'Linares', 'Longavi', 'Parral', 'Retiro', 'San Javier', 'Villa Alegre', 'Yerbas Buenas', 'Constitucion', 'Curepto', 'Empedrado', 'Maule', 'Pelarco', 'Pencahue', 'Rio Claro', 'San Clemente', 'San Rafael', 'Talca'],
    'Región del Ñuble': ['Bulnes', 'Chillan', 'Chillan Viejo', 'El Carmen', 'Pemuco', 'Pinto', 'Quillon', 'San Ignacio', 'Yungay', 'Cobquecura', 'Coelemu', 'Ninhue', 'Portezuelo', 'Quirihue', 'Ranquil', 'Treguaco', 'Coihueco', 'Ñiquen', 'San Carlos', 'San Fabian', 'San Nicolas'],
    'Región del Biobío': ['Arauco', 'Cañete', 'Contulmo', 'Curanilahue', 'Lebu', 'Los Alamos', 'Tirua', 'Alto Bio Bio', 'Antuco', 'Cabrero', 'Laja', 'Los Angeles', 'Mulchen', 'Nacimiento', 'Negrete', 'Quilaco', 'Quilleco', 'San Rosendo', 'Santa Barbara', 'Tucapel', 'Yumbel', 'Chiguayante', 'Concepcion', 'Coronel', 'Florida', 'Hualpen', 'Hualqui', 'Lota', 'Penco', 'San Pedro de la Paz', 'Santa Juana', 'Talcahuano', 'Tome'],
    'Región de La Araucanía': ['Carahue', 'Cholchol', 'Cunco', 'Curarrehue', 'Freire', 'Galvarino', 'Gorbea', 'Lautaro', 'Loncoche', 'Melipeuco', 'Nueva Imperial', 'Padre Las Casas', 'Perquenco', 'Pitrufquen', 'Pucon', 'Saavedra', 'Temuco', 'Teodoro Schmidt', 'Tolten', 'Vilcun', 'Villarrica', 'Angol', 'Collipulli', 'Curacautin', 'Ercilla', 'Lonquimay', 'Los Sauces', 'Lumaco', 'Puren', 'Renaico', 'Traiguen', 'Victoria'],
    'Región de Los Ríos': ['Futrono', 'La Union', 'Lago Ranco', 'Rio Bueno', 'Corral', 'Lanco', 'Los Lagos', 'Mafil', 'Mariquina', 'Paillaco', 'Panguipulli', 'Valdivia'],
    'Región de Los Lagos': ['Ancud', 'Castro', 'Chonchi', 'Curaco de Vélez', 'Dalcahue', 'Puqueldon', 'Queilen', 'Quellon', 'Quemchi', 'Quinchao', 'Calbuco', 'Cochamo', 'Fresia', 'Frutillar', 'Llanquihue', 'Los Muermos', 'Maullin', 'Puerto Montt', 'Puerto Varas', 'Osorno', 'Puerto Octay', 'Purranque', 'Puyehue', 'Rio Negro', 'San Pablo', 'San Juan de la Costa', 'Chaiten', 'Futaleufu', 'Hualaihue', 'Palena'],
    'Región Aisén del General Carlos Ibáñez del Campo': ['Aysen', 'Cisnes', 'Guaitecas', 'Cochrane', 'Ohiggins', 'Tortel', 'Coyhaique', 'Lago Verde', 'Chile Chico', 'Rio Ibañez'],
    'Región de Magallanes y la Antártica Chilena': ['Antartica', 'Laguna Blanca', 'Punta Arenas', 'Rio Verde', 'San Gregorio', 'Porvenir', 'Primavera', 'Timaukel', 'Puerto Natales', 'Torres del Paine']}

region = html.escape(form['region'].value)

if region not in regiones:
    Error = "Error en la región ingresada. Por favor, rellene nuevamente el formulario."

comuna = html.escape(form['comuna'].value)

if comuna not in dict_comunas[region]:
    Error = "Error en la comuna ingresada. Por favor, rellene nuevamente el formulario."

# Email

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

email = html.escape(form['email'].value, quote=True)

if (re.fullmatch(email_regex, email)) == None:
    Error = "Error en el email ingresado. Por favor, rellene nuevamente el formulario."

# Fechas

dia_hora_inicio = html.escape(form['dia-hora-inicio'].value, quote=True)
dia_hora_termino = html.escape(form['dia-hora-termino'].value, quote=True)

try:
    datetime.strptime(dia_hora_inicio, "%Y-%m-%d %H:%M")
except:
    Error = "Error con la fecha de inicio del evento. Por favor, rellene nuevamente el formulario."

try:
    datetime.strptime(dia_hora_termino, "%Y-%m-%d %H:%M")
except:
    Error = "Error con la fecha de término del evento. Por favor, rellene nuevamente el formulario."

# Tipo

tipos = ['Al Paso','Alemana', 'Árabe', 'Argentina', 'Asiática', 'Australiana',
    'Brasileña', 'Café y Snacks', 'Carnes',
    'Casera', 'Chilena',
    'China', 'Cocina de Autor', 'Comida Rápida', 'Completos', 'Coreana', 'Cubana',
    'Española', 'Exótica', 'Francesa', 'Gringa', 'Hamburguesa', 'Helados', 'India',
    'Internacional', 'Italiana', 'Latinoamericana', 'Mediterránea', 'Mexicana', 'Nikkei',
    'Parrillada', 'Peruana',
    'Pescados y mariscos', 'Picoteos',
    'Pizzas', 'Pollos y Pavos', 'Saludable',
    'Sándwiches', 'Suiza', 'Japonesa', 'Sushi',
    'Tapas', 'Thai', 'Vegana',
    'Vegetariana']

tipo = html.escape(form['tipo-comida'].value, quote=True)

if tipo not in tipos:
    Error = "Error en el tipo de comida del evento. Por favor, rellene nuevamente el formulario."

# Nombre

nombre = html.escape(form['nombre'].value, quote=True)
ln = len(nombre)
if ln < 4 or ln > 200:
    Error = "El nombre de contacto ingresado es muy largo, o muy corto en su defecto. Por favor rellene nuevamente el formulario"

# URLS

url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

tw = form.getvalue('twitter1', default=None)
ig = form.getvalue('instagram1', default=None)
fb = form.getvalue('facebook1', default=None)
tk = form.getvalue('tiktok1', default=None)
ot = form.getvalue('otra1', default=None)

# Twitter
if tw is not None: # si se relleno el input de twitter
    url_default = "https://www.twitter.com/"
    if tw.find('@') != -1 and tw.find('twitter'): # Si es un usuario y no tiene escrito la url en el
        tw.replace('@', '')
        url = url_default + tw
        if re.match(url_regex, url) == None:
            Error = "Error con el formato de su usuario de Twitter. Por favor, agregue un @ antes de su usuario (Ej: @nombreusuario)."
    else: # Si se ingreso una URL
        if re.match(url_regex, tw) == None:
            Error = "Error con el formato de su URL al perfil de Twitter. Por favor, ingrese un URL válido."

# Instagram
if ig is not None: # Si se relleno el input de instagram
    url_default = "https://www.instagram.com/"
    if ig.find('@') != -1 and ig.find('instagram'): # Si es un usuario y no tiene escrito la url en el
        ig.replace('@', '')
        url = url_default + ig
        if re.match(url_regex, url) == None:
            Error = "Error con el formato de su usuario de Instagram. Por favor, agregue un @ antes de su usuario (Ej: @nombreusuario)."
    else: # Si se ingreso una URL
        if re.match(url_regex, ig) == None:
            Error = "Error con el formato de su URL al perfil de Instagram. Por favor, ingrese un URL válido."

# Facebook
if fb is not None: # Si se relleno el input de facebook
    url_default = "https://www.facebook.com/"
    if fb.find('@') != -1 and fb.find('facebook'): # Si es un usuario y no tiene escrito la url en el
        fb.replace('@', '')
        url = url_default + fb
        if re.match(url_regex, url) == None:
            Error = "Error con el formato de su usuario de Facebook. Por favor, agregue un @ antes de su usuario (Ej: @nombreusuario)."
    else: # Si se ingreso una URL
        if re.match(url_regex, fb) == None:
            Error = "Error con el formato de su URL al perfil de Facebook. Por favor, ingrese un URL válido."

# Tik Tok
if tk is not None: # Si se relleno el input de tiktok
    url_default = "https://www.tiktok.com/"
    if tk.find('@') != -1 and tk.find('tiktok'): # Si es un usuario y no tiene escrito la url en el
        url = url_default + tk
        if re.match(url_regex, url) == None:
            Error = "Error con el formato de su usuario de TikTok. Por favor, agregue un @ antes de su usuario (Ej: @nombreusuario)."
    else: # Si se ingreso una URL
        if re.match(url_regex, tk) == None:
            Error = "Error con el formato de su URL al perfil de TikTok. Por favor, ingrese un URL válido."

# Otra
if ot is not None:
    if ot.find('@') != -1: # Si se ingreso un nombre de usuario
        Error = "Error con el formato de 'Otra red social'. Por favor, ingrese una URL válida a su perfil. No ingrese un usuario."
    else:
        if re.match(url_regex, ot) == None:
            Error = Error = "Error con el formato de 'Otra red social'. Por favor, ingrese una URL válida a su perfil."

#Fotos

cant_fotos = len(form.getlist('foto-comida'))

if  cant_fotos == 1:
    foto = form['foto-comida']
    nombre_archivo = foto.filename
    if not nombre_archivo:
        Error= "Usted no ha enviado un archivo en el formulario"
        
    MAX_FILE_SIZE = 100000 * 1000 # 100MB
    size_archivo = os.fstat(foto.file.fileno()).st_size # vemos el tamaño del archivo
    if size_archivo >= MAX_FILE_SIZE:
        Error= "Uno de sus archivos pesa demasiado. Por favor, verifique que el peso de cada archivo no sea mayor a 100MB."
        
    tipo_archivo = filetype.guess(foto.file) # vemos el tipo de archivo
    foto.file.seek(0, 0)  # devolver el puntero al inicio del archivo
    if (tipo_archivo.mime != 'image/jpeg') and (tipo_archivo.mime  != 'image/png'): # si el tipo de archivo no corresponde al pedido
        Error= "Uno de los archivos no corresponde al tipo correcto. Por favor, cerciórese de que estos sean de tipo JPG, JPEG o PNG."

else:
    for foto in form["foto-comida"]: # lista con las fotos enviadas
        nombre_archivo = foto.filename # vemos el nombre del archivo
        if not nombre_archivo: # si no tiene nombre el archivo // no ha enviado archivo
            Error= "Usted no ha enviado un archivo en el formulario"

        MAX_FILE_SIZE = 100000 * 1000 # 100MB
        size_archivo = os.fstat(foto.file.fileno()).st_size # vemos el tamaño del archivo
        if size_archivo >= MAX_FILE_SIZE:
            Error= "Uno de sus archivos pesa demasiado. Por favor, verifique que el peso de cada archivo no sea mayor a 100MB."

        tipo_archivo = filetype.guess(foto.file) # vemos el tipo de archivo
        foto.file.seek(0, 0)  # devolver el puntero al inicio del archivo
        if (tipo_archivo.mime != 'image/jpeg') and (tipo_archivo.mime  != 'image/png'): # si el tipo de archivo no corresponde al pedido
            Error= "Uno de los archivos no corresponde al tipo correcto. Por favor, cerciórese de que estos sean de tipo JPG, JPEG o PNG."

if Error != "": # Si hubo errores
    head = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Estas siendo redirigido...</title>
        <link rel="stylesheet" href="../../Tarea3/estilos.css">
        <meta http-equiv="refresh" content="8;url='https://anakena.dcc.uchile.cl/~bpezoa/Tarea3/form.html'">
    </head>
    <body>
        <div class='main'>
    '''
    print(head, file=utf8stdout)
    
    print(" <p> Su formulario ha fallado: " + Error + "</p>", file=utf8stdout)

    bottom = '''
             <p> Si no ha sido redirigido en 8seg. haga click <a href='https://anakena.dcc.uchile.cl/~bpezoa/Tarea3/form.html'>aquí</a> </p>
        </div>
    </body>
    </html>
    '''
    print(bottom, file=utf8stdout)

else: # Si no hubo errores

    if cant_fotos == 1:
        data = (
        form['region'].value,
        form['comuna'].value,
        form['sector'].value,
        form['nombre'].value,
        form['email'].value,
        form['celular'].value,
        form.getvalue('twitter1', default='No'),
        form.getvalue('instagram1', default='No'),
        form.getvalue('facebook1', default='No'),
        form.getvalue('tiktok1', default='No'),
        form.getvalue('otra1', default='No'),
        form['dia-hora-inicio'].value,
        form['dia-hora-termino'].value,
        form['descripcion-evento'].value,
        form['tipo-comida'].value,
        foto
        )

    else:

        data = (
            form['region'].value,
            form['comuna'].value,
            form['sector'].value,
            form['nombre'].value,
            form['email'].value,
            form['celular'].value,
            form.getvalue('twitter1', default='No'),
            form.getvalue('instagram1', default='No'),
            form.getvalue('facebook1', default='No'),
            form.getvalue('tiktok1', default='No'),
            form.getvalue('otra1', default='No'),
            form['dia-hora-inicio'].value,
            form['dia-hora-termino'].value,
            form['descripcion-evento'].value,
            form['tipo-comida'].value,
        )
        for foto in form['foto-comida']: # lista con todos los valores enviados bajo el name "foto-comida"
            data= data + (foto, )

    Eventdb = db.Evento("localhost", "cc500209_u", "usvestibul", "cc500209_db") # Establecemos conexion con la base despues de haber verificado los inputs

    if len(form) > 0 and Error == "": # si se ha enviado el formulario y no hay errores
        insert = Eventdb.save_event(data) # insertamos la informacion en la base

    head = f'''
    <!-- HTML5 -->
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Estas siendo redirigido...</title>
        <link rel="stylesheet" href="../../Tarea3/estilos.css">
        <meta http-equiv="refresh" content="8;url='https://anakena.dcc.uchile.cl/~bpezoa/cgi-bin/Tarea3/index.py'">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    </head>

    <body>
    '''
    print(head, file=utf8stdout)

    body = f'''
    <div class="main">
        <div class="negrita">
        <p class="negrita" style="text-align: "centered";"> Su evento se ha listado con éxito! </p>
        <p> Ahora será redirigido a la portada en 8seg.</p>
        <p> Si usted no está siendo redirigido, por favor, haga click <a href='https://anakena.dcc.uchile.cl/~bpezoa/cgi-bin/Tarea3/index.py'>aquí</a></p>
        </div>
    </div>
    '''

    print(body, file=utf8stdout)

    bottom = f'''

    <script src="../../Tarea3/scriptTarea.js"></script>

    </body>

    </html>
    '''

    print(bottom, file=utf8stdout)
