const mate = ['Álgebra','Geometría','Cálculo']
const esp = ['Lectura y Redacción','Literatura']
const ciencia = ['Biología','Química','Medicina']
const hum = ['Historia','Filosofía','Psicología']

$(function (){
    var sel_mat = $('select[name="Tema"]')
    sel_mat.prop('disabled',true);                  //Por default desabilita el segundo dropdownlist
    $('select[name="Materia"]').change(function (){//Cuando se selecciona un elemento del primer dropdownlist
        var list;
        var select = document.getElementById("Tema");
        var selectElement = document.querySelector('#Materias');
        switch(selectElement.value){//Identifica qué Materia fue seleccionada
            case "Matemáticas":
                list = createList(mate,3);
            break;
            case "Español":
                list = createList(esp,2);
            break;
            case "Ciencias Naturales":
                list = createList(ciencia,3);
            break;
            case "Humanidades":
                list = createList(hum,3);
            break;
        }

        //Dos formas de limpiar la dropdownlist
        /*var len = select.length;
        for(var i=len -1;i>=0; i--){
            select.remove(i);
        }*/
        $("#Tema").empty();                             //Limpia los elementos de la dropdownlist de Tema

        for(var i=0;i<list.length;i++){
            var op = list[i];                           //Almacena el tema
            var el = document.createElement("option");  //Crea una nueva opción
            el.textContent = op;                        //Contenido
            el.value = op;                              
            select.appendChild(el);
        }
        sel_mat.prop('disabled',false);             //Habilita el segundo dropdownlist
    });
});

function createList(materia,len){
    var list = [];
    for(var i=0;i<len;i++){
        list.push(materia[i]);
    }
    return list; 
}