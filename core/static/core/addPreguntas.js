//variables contadoras para agregar a mi formulario
// let ab = 1; //pregunta abierta counter
// let ce = 1; //pregunta cerrada counter
const LIMITE_OPCIONES = 6;

//getting add question buttons and assign them 'onclick' event
const divPregunta = document.querySelector(".Preguntas");//Padre

const addPregAbierta = document.querySelector(".addPregAbierta");
const totalAbForms = document.getElementById("id_abiertas-TOTAL_FORMS");
const currAbiertas = document.getElementsByClassName("pregAbierta");

const addPregCerrada = document.querySelector(".addPregCerrada");
const totalCeForms = document.getElementById("id_cerradas-TOTAL_FORMS");
const currCerradas = document.getElementsByClassName("pregCerrada");

const totalResp = document.getElementById("id_cerradas-__prefix__-respuestacerrada_set-TOTAL_FORMS");
const currRespuestas = document.getElementsByClassName("respCerradas");

const regex = new RegExp('__prefix__','g');

function createPregAbierta(){
    let abCount = currAbiertas.length;
    let abTarget = document.querySelector('.abiertas-list');//abiertaTarget
    //copying the empty form for preguntaAbierta
    const cpyEmptyAb = document.querySelector("#empty-ab").cloneNode(true);
    cpyEmptyAb.setAttribute('class','pregAbierta');
    cpyEmptyAb.setAttribute('id',`abiertas-${abCount}`);
    cpyEmptyAb.innerHTML = cpyEmptyAb.innerHTML.replace(regex,abCount);
    totalAbForms.setAttribute('value',abCount+1);

    //addding the empty form element to the html
    abTarget.append(cpyEmptyAb);
}
function createRespCerrada(){
    let respCount;
    const cpyEmptyResp = document.querySelector("#empty-resp").cloneNode(true);
}
function createPregCerrada(){
    let ceCount = currCerradas.length;
    let ceTarget = document.querySelector('.cerradas-list');//cerradaTarget
    //boton que agrega una nueva respuesta
    const btn = document.createElement("button");
    btn.innerHTML = "Añadir respuesta";
    btn.type = "button";
    btn.id = "btnAddRespuesta";
    btn.addEventListener("click",(event)=>{
        if(event){
            event.preventDefault();
        }
        createRespCerrada();
    })
    //copyting the empty form for preguntaCerrada
    const cpyEmptyCe = document.querySelector("#empty-ce").cloneNode(true);
    cpyEmptyCe.setAttribute('class','pregCerrada');
    cpyEmptyCe.setAttribute('id',`cerradas-${ceCount}`);
    cpyEmptyCe.innerHTML = cpyEmptyCe.innerHTML.replace(regex,ceCount);
    totalCeForms.setAttribute('value',ceCount+1);

    ceTarget.append(cpyEmptyCe);
    ceTarget.append(btn);
    
}

//EVENT LISTENERS
addPregAbierta.addEventListener("click",(event)=>{
    // console.log("Añadiendo una pregunta ABIERTA");
    if(event){
        event.preventDefault();
    }
    createPregAbierta();
    console.log("presionado xd");
});

addPregCerrada.addEventListener("click",(event)=>{
    // console.log("Añadiendo una pregunta CERRADA");
    if(event){
        event.preventDefault();
    }
    createPregCerrada();
    console.log("Cerradaaaas lel");
});