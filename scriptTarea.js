function validador() {

    let region = document.getElementsByName('region')[0];
    let comuna = document.getElementsByName('comuna')[0];
    let sector = document.getElementsByName('sector')[0];
    let nombre = document.getElementsByName('nombre')[0];
    let email = document.getElementsByName('email')[0];
    let celular = document.getElementsByName('celular')[0];
    let dia_inicio = document.getElementsByName('dia-hora-inicio')[0];
    let dia_termino = document.getElementsByName('dia-hora-termino')[0];
    let tipo = document.getElementsByName('tipo-comida')[0];
    let fotos = document.getElementsByName('foto-comida');

    let ig = document.getElementById('instagram1');
    let tw = document.getElementById('twitter1');
    let fb = document.getElementById('facebook1');
    let tk = document.getElementById('tiktok1');
    let ot = document.getElementById('otra1');


    let tipos = ['Al Paso','Alemana', 'Árabe', 'Argentina', 'Asiática', 'Australiana',
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
    'Vegetariana'];

    let regiones = ['Región Arica y Parinacota', 'Región de Tarapacá', 'Región de Antofagasta',
    'Región de Atacama', 'Región de Coquimbo', 'Región de Valparaiso', 'Región Metropolitana de Santiago',
    'Región del Libertador General Bernardo Ohiggins', 'Región del Maule', 'Región del Ñuble',
    'Región del Biobío', 'Región de La Araucanía', 'Región de Los Ríos', 'Región de Los Lagos',
    'Región Aisén del General Carlos Ibáñez del Campo', 'Región de Magallanes y la Antártica Chilena'];

    let comunas = ['Arica', 'Camarones', 'Gral. Lagos', 'Putre',
    'Alto Hospicio', 'Iquique', 'Camiña', 'Colchane', 'Huara', 'Pica', 'Pozo Almonte',
    'Antofagasta', 'Mejillones', 'Sierra Gorda', 'Taltal', 'Calama', 'Ollague', 'San Pedro Atacama', 'Maria Elena', 'Tocopilla',
    'Chañaral', 'Diego de Almagro', 'Caldera', 'Copiapo', 'Tierra Amarilla', 'Alto del Carmen', 'Freirina', 'Huasco', 'Vallenar',
    'Canela', 'Illapel', 'Los Vilos', 'Salamanca', 'Andacollo', 'Coquimbo', 'La Higuera', 'La Serena', 'Paihuano', 'Vicuña', 'Combarbala', 'Monte Patria', 'Ovalle', 'Punitaqui', 'Rio Hurtado',
    'Isla de pascua', 'Calle Larga', 'Los Andres', 'Rinconada de Los Andes', 'San Esteban', 'Limache', 'Olmue', 'Quilpue', 'Villa Alemana', 'Cabildo', 'La Ligua', 'Papudo', 'Petorca', 'Zapallar', 'Hijuela', 'La Calera', 'La Cruz', 'Nogales', 'Quillota', 'Algarrobo', 'Cartagena', 'El Quisco', 'El Tabo', 'San Antonio', 'Santo Domingo', 'Catemu', 'Llay Llay', 'Panquehue', 'Putaendo', 'San Felipe', 'Santa María', 'Casablanca', 'Concon', 'Juan Fernandez', 'Puchuncavi', 'Quintero', 'Valparaiso', 'Viña del Mar',
    'Colina', 'Lampa', 'Tiltil', 'Pirque', 'Puente Alto', 'San Jose de Maipo', 'Buin', 'Calera de Tango', 'Paine', 'San Bernardo', 'Alhue', 'Curacavi', 'Maria Pinto', 'Melipilla', 'San Pedro', 'Cerrillos', 'Cerro Navia', 'Conchali', 'El Bosque', 'Estacion Central', 'Huechuraba', 'Independencia', 'La Cisterna', 'La Granja', 'La Florida', 'La Pintana', 'La Reina', 'Las Condes', 'Lo Barnechea', 'Lo Espejo', 'Lo Prado', 'Macul', 'Maipu', 'Ñuñoa', 'Pedro Aguirre Cerda', 'Peñalolen', 'Providencia', 'Pudahuel', 'Quilicura', 'Quinta Normal', 'Recoleta', 'Renca', 'San Miguel', 'San Joaquin', 'San Ramon', 'Santiago', 'Vitacura', 'El Monte', 'Isla de Maipo', 'Padre Hurtado', 'Peñaflor', 'Talagante',
    'Codegua', 'Coinco', 'Coltauco', 'Doñihue', 'Graneros', 'Las Cabras', 'Machali', 'Malloa', 'Olivar', 'Peumo', 'Pichidegua', 'Quinta Tilcoco', 'Rancagua', 'Requinoa', 'Rengo', 'Mostazal', 'San Vicente', 'La Estrella', 'Litueche', 'Marchigue', 'Navidad', 'Paredones', 'Pichilemu', 'Chepica', 'Chimbarongo', 'Lolol', 'Nancagua', 'Palmilla', 'Peralillo', 'Placilla', 'Pumanque', 'San Fernando', 'Santa Cruz',
    'Curico', 'Hualañe', 'Licanten', 'Molina', 'Rauco', 'Romeral', 'Sagrada Familia', 'Teno', 'Vichuquen', 'Colbun', 'Linares', 'Longavi', 'Parral', 'Retiro', 'San Javier', 'Villa Alegre', 'Yerbas Buenas', 'Constitucion', 'Curepto', 'Empedrado', 'Maule', 'Pelarco', 'Pencahue', 'Rio Claro', 'San Clemente', 'San Rafael', 'Talca',
    'Bulnes', 'Chillan', 'Chillan Viejo', 'El Carmen', 'Pemuco', 'Pinto', 'Quillon', 'San Ignacio', 'Yungay', 'Cobquecura', 'Coelemu', 'Ninhue', 'Portezuelo', 'Quirihue', 'Ranquil', 'Treguaco', 'Coihueco', 'Ñiquen', 'San Carlos', 'San Fabian', 'San Nicolas',
    'Arauco', 'Cañete', 'Contulmo', 'Curanilahue', 'Lebu', 'Los Alamos', 'Tirua', 'Alto Bio Bio', 'Antuco', 'Cabrero', 'Laja', 'Los Angeles', 'Mulchen', 'Nacimiento', 'Negrete', 'Quilaco', 'Quilleco', 'San Rosendo', 'Santa Barbara', 'Tucapel', 'Yumbel', 'Chiguayante', 'Concepcion', 'Coronel', 'Florida', 'Hualpen', 'Hualqui', 'Lota', 'Penco', 'San Pedro de la Paz', 'Santa Juana', 'Talcahuano', 'Tome',
    'Carahue', 'Cholchol', 'Cunco', 'Curarrehue', 'Freire', 'Galvarino', 'Gorbea', 'Lautaro', 'Loncoche', 'Melipeuco', 'Nueva Imperial', 'Padre Las Casas', 'Perquenco', 'Pitrufquen', 'Pucon', 'Saavedra', 'Temuco', 'Teodoro Schmidt', 'Tolten', 'Vilcun', 'Villarrica', 'Angol', 'Collipulli', 'Curacautin', 'Ercilla', 'Lonquimay', 'Los Sauces', 'Lumaco', 'Puren', 'Renaico', 'Traiguen', 'Victoria',
    'Futrono', 'La Union', 'Lago Ranco', 'Rio Bueno', 'Corral', 'Lanco', 'Los Lagos', 'Mafil', 'Mariquina', 'Paillaco', 'Panguipulli', 'Valdivia',
    'Ancud', 'Castro', 'Chonchi', 'Curaco de Vélez', 'Dalcahue', 'Puqueldon', 'Queilen', 'Quellon', 'Quemchi', 'Quinchao', 'Calbuco', 'Cochamo', 'Fresia', 'Frutillar', 'Llanquihue', 'Los Muermos', 'Maullin', 'Puerto Montt', 'Puerto Varas', 'Osorno', 'Puerto Octay', 'Purranque', 'Puyehue', 'Rio Negro', 'San Pablo', 'San Juan de la Costa', 'Chaiten', 'Futaleufu', 'Hualaihue', 'Palena',
    'Aysen', 'Cisnes', 'Guaitecas', 'Cochrane', 'Ohiggins', 'Tortel', 'Coyhaique', 'Lago Verde', 'Chile Chico', 'Rio Ibañez',
    'Antartica', 'Laguna Blanca', 'Punta Arenas', 'Rio Verde', 'San Gregorio', 'Porvenir', 'Primavera', 'Timaukel', 'Puerto Natales', 'Torres del Paine'];

    let regexEmail = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    let regexCelular = /^(\+?56)?(\s?)(0?9)(\s?)[9876543]\d{7}$/im;
    let regexFecha = /[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/;
    let regexUrl = new RegExp('^(https?:\\/\\/)?'+ // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
    '(\\#[-a-z\\d_]*)?$','i'); // fragment locator


    let error = document.getElementById('error');
    error.innerHTML = 'Su formulario falló en: ';

    let status = true;

    if (region.value == "" || !(regiones.includes(region.value))) {
        error.innerHTML += 'Región\n';
        region.style = 'border:1px solid red';
        status = false;
    } else {
        region.style = 'border:1px solid green';
    }

    if (comuna.value == "" || !(comunas.includes(comuna.value))) {
        error.innerHTML += 'Comuna\n';
        comuna.style = 'border:1px solid red';
        status = false;
    } else {
        comuna.style = 'border:1px solid green';
    }

    if (sector.value.length > 100) {
        error.innerHTML += 'Sector\n';
        sector.style = 'border:1px solid red';
        status = false;
    } else {
        sector.style = 'border:1px solid green';
    }

    if (nombre.value.length > 200 || nombre.value.length <4) {
        error.innerHTML += 'Nombre\n';
        nombre.style = 'border:1px solid red';
        status = false;
    } else {
        nombre.style = 'border:1px solid green';
    }

    if (!(regexEmail.test(email.value))) {
        error.innerHTML += 'E-mail\n';
        email.style = 'border:1px solid red';
        status = false;
    } else {
        email.style = 'border:1px solid green';
    }

    if (!(regexCelular.test(celular.value))) {
        error.innerHTML += 'Celular\n';
        celular.style = 'border:1px solid red';
        status = false;
    } else {
        celular.style = 'border:1px solid green';
    }

    if (tipo.value == "" || !(tipos.includes(tipo.value))) {
        error.innerHTML += 'Tipo\n';
        tipo.style = 'border:1px solid red';
        status = false;
    } else {
        tipo.style = 'border:1px solid green';
    }

    if (!(regexFecha.test(dia_inicio.value))) {
        error.innerHTML += 'Día y Hora inicio \n';
        dia_inicio.style = 'border:1px solid red';
        status = false;
    } else {
        dia_inicio.style = 'border:1px solid green';
    }

    if (!(regexFecha.test(dia_termino.value))) {
        error.innerHTML += 'Día y Hora termino \n';
        dia_termino.style = 'border:1px solid red';
        status = false;
    } else {
        dia_termino.style = 'border:1px solid green';
    }

    if (fotos[0].value == "" || fotos.length > 5) {
        error.innerHTML += 'Fotos\n';
        dia_termino.style = 'border:1px solid red';
        status = false;
    } else {
        dia_termino.style = 'border:1px solid green';
    }

    if (!status) {
        error.style = 'display:block';
    }

    // Al llegar aca, se envia el formulario
    return status;
}

// Confirmar el envio del formulario
function confirmacionEnvio() {
    alert("Hemos recibido su información, muchas gracias y suerte en su enprendimiento!");
    document.getElementById("formulario").submit();
}

// Prellenar la fecha inicial

let today = new Date();
let month = parseInt(today.getMonth()+1);
document.getElementById('dia-hora-inicio').value = today.getFullYear() + "-" +
    + (month<10?('0'+month):month) + "-" + (today.getDate()<10?'0':'') + today.getDate() + 
    " " + (today.getHours()<10?'0':'') + today.getHours() + ":" + 
    (today.getMinutes()<10?'0':'') + today.getMinutes();

// Click en imagen la muestra en 840x600
function agrandarImagen(imagen) {
    img = document.getElementById(imagen);
    img.style.width = "600px";
    img.style.height = "800px ";
    img.style.transition = "width 0.5s ease";
}

// Boton que permite achicar la imagen a su resolucion principal
function resetImagen(imagen) {
    img = document.getElementById(imagen);
    img.style.width = "240px";
    img.style.height = "320px";
    img.style.transition = "width 0.5s ease";
}


// Comunas en base a region
var lookup = {
   'Región Arica y Parinacota': ['Arica', 'Camarones', 'Gral. Lagos', 'Putre'],
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
    'Región de Magallanes y la Antártica Chilena': ['Antartica', 'Laguna Blanca', 'Punta Arenas', 'Rio Verde', 'San Gregorio', 'Porvenir', 'Primavera', 'Timaukel', 'Puerto Natales', 'Torres del Paine'],
};

// Modal de confirmacion
$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus');
})

// Modal
var modal = document.getElementById("myModal");

// Boton que abre el modal
var btn = document.getElementById("myBtn");

// Al hacer click en enviar formulario, abrir el modal
btn.onclick = function() {
    if (validador()) {
        modal.style.display = "block";
    } else {
        return validador();
    }
}

// Para cerrar el modal
function cerrar() {
  modal.style.display = "none";
}

// Al cliquear fuera del modal, este se cierra
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Mostrar comunas en base a la region seleccionada
$('#region').on('change', function() {
    var selectValue = $(this).val();
    $('#comuna').empty();
    for (i = 0; i < lookup[selectValue].length; i++) {
        $('#comuna').append("<option value='" + lookup[selectValue][i] + "'>" + lookup[selectValue][i] + "</option>");
    }
});

// Boton para agregar mas imagenes
let totalagregados = 0;

$(document).ready(function(){
    $('.add_more').click(function(e){
        e.preventDefault();
        if (totalagregados<=3){
            $(this).before("<input name='foto-comida' type='file'>");
            totalagregados+=1;
        } else {
            document.getElementById('add_more').style.display = "none";
        } 
    });
});


// Deshabilitar input de RRSS hasta seleccionar una opcion
function chequear(id){
    let checkbox = document.getElementById(id);
    var text = id + "1";
    if (checkbox.checked == true){
        $('#' + id).before("   <input name='" + text + "' id='" + text + "' type='text' placeholder='Ingrese su @usuario o URL al perfil'>");
    } else {
        var input = document.getElementById(text)
        input.parentNode.removeChild(input)
    }
}

const btnMenu = Array.from(document.querySelectorAll('.btn-menu'));

btnMenu.forEach((btns) => {
    btns.addEventListener('click', () => {
        btnMenu.forEach((btns) => {
            btns.classList.remove('selected');
        });
        btns.classList.add('selected');
    });
});

// Mostrar toda la info al hacer click sobre la tabla

function moreInfo(id){
    return window.location='evento_particular.py?' + "ident=" + String(id);
}


// paginacion

jQuery(function($) {
    // Consider adding an ID to your table
    // incase a second table ever enters the picture.
    var items = $("#table content tbody tr");

    var numItems = items.length;
    var perPage = 2;

    // Only show the first 2 (or first `per_page`) items initially.
    items.slice(perPage).hide();

    // Now setup the pagination using the `.pagination-page` div.
    $("#pagination").pagination({
        items: numItems,
        itemsOnPage: 2,
        cssStyle: "light-theme",

        // This is the actual page changing functionality.
        onPageClick: function(pageNumber) {
            // We need to show and hide `tr`s appropriately.
            var showFrom = perPage * (pageNumber - 1);
            var showTo = showFrom + perPage;

            // We'll first hide everything...
            items.hide()
                 // ... and then only show the appropriate rows.
                 .slice(showFrom, showTo).show();
        }
    });

});

