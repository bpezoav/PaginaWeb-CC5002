// AJAX para graficos
$(document).ready(function () { // al momento de estar cargado el documento, se ejecuta la sig. funcion
    let xhttp = new XMLHttpRequest(); // creamos un nuevo xhr
    let query = new FormData();
    query.append('tipo', 'eventosxdia');
    xhttp.open('POST', '../cgi-bin/Tarea3/querys.py'); // A donde se realiza la peticion 
    xhttp.onreadystatechange = function () { // si la respestua cambia su estado
        if (xhttp.readyState == 4 && xhttp.status == 200) { // si la peticion esta lista y salio correctamente
            var data = JSON.parse(xhttp.response);
            var rows = "";
            for (var key in data) {
                let value = data[key];
                rows += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td>" + "</tr>"; // agregamos los datos a la tabla correspondiente
            }
            $(rows).appendTo("#dataEventos tbody");

            Highcharts.chart('eventos-por-dia', {
                title: {
                    text: 'Eventos por dia'
                },
                data: {
                    table: 'dataEventos'
                },
                yAxis: {
                    title: {
                        text: 'Cantidad'
                    }
                },
                xAxis: {
                    title: {
                        text: 'Fecha'
                    }
                },
                plotOptions: {
                    series: {
                        marker: {
                            enabled: true
                        }
                    }
                },
                title: {
                    text: 'Eventos por dia'
                }
            });
        }
    };
    xhttp.send(query); // Mandamos la peticion

    // 2da Request, grafico de torta

    const xhttp2 = new XMLHttpRequest(); // creamos un nuevo xhr
    let query2 = new FormData();
    query2.append('tipo', 'torta')
    xhttp2.open('POST', '../cgi-bin/Tarea3/querys.py'); // A donde se realiza la peticion 
    xhttp2.onreadystatechange = function () { // si la respestua cambia su estado
        if (xhttp2.readyState == 4 && xhttp2.status == 200) { // si la peticion esta lista y salio correctamente
            var data = JSON.parse(xhttp2.response);
            var rows = "";
            for (var key in data) {
                let value = data[key];
                rows += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td>" + "</tr>"; // agregamos los datos a la tabla correspondiente
            }
            $(rows).appendTo("#dataTipo tbody");

            Highcharts.chart('eventos-por-tipo', {
                chart: {
                    type: 'pie'
                },
                title: {
                    text: 'Eventos por tipo'
                },
                data: {
                    table: 'dataTipo'
                },
                yAxis: {
                    title: {
                        text: 'Cantidad'
                    }
                },
                xAxis: {
                    title: {
                        text: 'Tipo'
                    }
                },
                plotOptions: {
                    pie: {
                        allowPointSelect: true,
                        cursor: 'pointer',
                        dataLabels: {
                            enabled: true,
                            format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                        }
                    }
                },
                title: {
                    text: 'Eventos por Tipo'
                }
            });
        }
    };
    xhttp2.send(query2); // Mandamos la peticion

    // 3ra Request, grafico de 3 barras por fecha

    const xhttp3 = new XMLHttpRequest(); // creamos un nuevo xhr
    let query3 = new FormData();
    query3.append('tipo', 'barras')
    xhttp3.open('POST', '../cgi-bin/Tarea3/querys.py'); // A donde se realiza la peticion 
    xhttp3.onreadystatechange = function () { // si la respestua cambia su estado
        if (xhttp3.readyState == 4 && xhttp3.status == 200) { // si la peticion esta lista y salio correctamente
            var data = JSON.parse(xhttp3.response);
            var rows = "";
            for (var key in data) {
                let value = data[key];
                rows += "<tr><td>" + value[0] + "</td><td>" + value[1] + "</td>" + "<td>" + value[2] + "</td><td>" + value[3] + "</td></tr>"; // agregamos los datos a la tabla correspondiente
            }
            $(rows).appendTo("#dataHora tbody");

            Highcharts.chart('eventos-por-hora', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Eventos por hora de inicio'
                },
                data: {
                    table: 'dataHora'
                },
                yAxis: {
                    title: {
                        text: 'Cantidad'
                    }
                },
                xAxis: {
                    title: {
                        text: 'Fecha'
                    }
                },
                plotOptions: {
                },
                title: {
                    text: 'Eventos por Hora de inicio'
                }
            });
        }
    };
    xhttp3.send(query3); // Mandamos la peticion
})