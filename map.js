// Mapa de eventos

//const tilesProvider = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

const tilesProvider = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYmFzdGkxODU0IiwiYSI6ImNrdnhpMXRyaDlxNTQybnExbmV5ZGhjNmsifQ.lTpei0rnNl-9ywYmHbfyiA'

var mymap = L.map('map').setView([-33.4500000, -70.6666667], 13);

// 
L.tileLayer(tilesProvider, {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'your.mapbox.access.token'
}).addTo(mymap);

var popup = L.popup()



// Funcion para añadir marcadores
function addMark(row){
    var lat = parseFloat(row[4][0]);
    var long = parseFloat(row[4][1]);
    var fotos = row[3];
    var qnt = "Cantidad de fotos: ";
    qnt = qnt.concat(fotos.length);

    // Tabla
    var table = ''
    table += '<table><tr><th>Fecha inicio - (Año-Mes-Dia) </th><th>Tipo de comida</th><th>Sector</th><th>Fotos</th><th>Informacion</th></tr>'
    
    // Agregamos la info a la tabla
    table += '<tr>'
    // Añadimos la fecha
    table += '<td>' + row[0] + '</td>'
    // Añadimos el tipo de comida
    table += '<td>' + row[1] + '</td>'
    // Añadimos el sector
    table += '<td>' + row[2] + '</td>'
    // Añadimos las fotos
    table += '<td>'
    for (var i =0; i<fotos.length ; i++){
        table += '<img src="../' + row[3][i] + '" height="75" width="75">'
    }
    table += '</td>'
    // Creamos el link para obtener la info del evento
    table += '<td>' + '<a href="evento_particular.py?ident=' + row[5] + '" target="_blank">Ir al evento</a></td>'
    table += '</tr>'

    //Creamos el marcador
    var marker = L.marker([lat, long]).addTo(mymap);

    // Cantidad de fotos al poner el mouse encima
    marker.bindTooltip(qnt).openPopup();

    // Contenido del popup al hacer click
    marker.bindPopup(table, {maxWidth: 500 }).openPopup();
}

// Abrimos una request a la DB con metodo GET para obtener las comunas de los eventos
$(document).ready(function() { // al momento de estar cargado el documento, se ejecuta la sig. funcion
    let xhttp = new XMLHttpRequest(); // creamos un nuevo xhr
    xhttp.open('GET', './mapa.py'); // A donde se realiza la peticion 
    xhttp.onreadystatechange = function () { // si la respestua cambia su estado
        if (xhttp.readyState == 4 && xhttp.status == 200) { // si la peticion esta lista y salio correctamente
            var data = JSON.parse(xhttp.response);
            console.log(data);
            for (var i = 0; i<data.length ; i++){
                addMark(data[i]);
            }
        }
    }
    xhttp.send();
});

