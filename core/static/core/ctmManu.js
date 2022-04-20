console.log("Sheeesh");

$('#pregunta').hide();

var contenedor = document.getElementById('preguntas-container');

$('#preguntaAbierta').click(function() {
    var encabezadoPregunta = document.createElement('label');
    encabezadoPregunta.innerHTML = 'Pregunta: '
    var preguntaPlanteamiento = document.createElement('input');
    preguntaPlanteamiento.setAttribute('id', 'id_planteamiento');
    preguntaPlanteamiento.setAttribute('type', 'text');
    preguntaPlanteamiento.setAttribute('name', 'planteamiento');
    preguntaPlanteamiento.setAttribute('maxlength', '100');


    var encabezadoRespuesta = document.createElement('label');
    encabezadoRespuesta.innerHTML = 'Respuesta: '
    var preguntaRespuesta = document.createElement('input');
    preguntaRespuesta.setAttribute('id', 'id_respuesta');
    preguntaRespuesta.setAttribute('type', 'text');
    preguntaRespuesta.setAttribute('name', 'respuesta');
    preguntaRespuesta.setAttribute('maxlength', '100');
    var saltoLinea = document.createElement('br');

    contenedor.appendChild(encabezadoPregunta);
    contenedor.appendChild(preguntaPlanteamiento);
    contenedor.appendChild(encabezadoRespuesta);
    contenedor.appendChild(preguntaRespuesta);
    contenedor.appendChild(saltoLinea);
})
