//variables contadoras para agregar a mi formulario
const LIMITE_OPCIONES = 6;
let op = 2; //opcion counter
//getting add question buttons and assign them 'onclick' event
const divPregunta = document.querySelector(".Preguntas");//Padre

const addPregAbierta = document.querySelector(".addPregAbierta");
const totalAbForms = document.getElementById("id_abiertas-TOTAL_FORMS");
const currAbiertas = document.getElementsByClassName("pregAbierta");

const addPregCerrada = document.querySelector(".addPregCerrada");
const totalCeForms = document.getElementById("id_cerradas-TOTAL_FORMS");
const currCerradas = document.getElementsByClassName("pregCerrada");

const totalResp = document.getElementById("id_respCerradas-TOTAL_FORMS");
const currRespuestas = document.getElementsByClassName("respCerrada");

const regex = new RegExp('__prefix__','g');
const regOpc = new RegExp('__num__','g');

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
// function createRespCerrada(){
//     let respCount = currRespuestas.length;
//     console.log(respCount);
//     let respTarget = document.querySelector(".respCerradas-list");
//     if(respCount >= LIMITE_OPCIONES){
//         alert("Solo puedes ingresar hasta 6 opciones diferentes");
//     }
//     const cpyEmptyResp = document.querySelector("#empty-resp").cloneNode(true);
//     cpyEmptyResp.setAttribute('class','respCerrada');
//     cpyEmptyResp.setAttribute('id',`respCerrada-${respCount}`);
//     cpyEmptyResp.innerHTML = cpyEmptyResp.innerHTML.replace(regex,respCount);
//     cpyEmptyResp.innerHTML = cpyEmptyResp.innerHTML.replace(regOpc,op);
//     totalResp.setAttribute('value',respCount+1);

//     //appending
//     respTarget.append(cpyEmptyResp);
// }
function createPregCerrada(){
    let ceCount = currCerradas.length;
    let ceTarget = document.querySelector('.cerradas-list');//cerradaTarget
    //boton que agrega una nueva respuesta
    // const btn = document.createElement("button");
    // btn.innerHTML = "Añadir respuesta";
    // btn.type = "button";
    // btn.id = "btnAddRespuesta";
    // btn.addEventListener("click",(event)=>{
    //     if(event){
    //         event.preventDefault();
    //     }
    //     createRespCerrada();
    // })
    //copying the empty form for preguntaCerrada
    const cpyEmptyCe = document.querySelector("#empty-ce").cloneNode(true);
    cpyEmptyCe.setAttribute('class','pregCerrada');
    cpyEmptyCe.setAttribute('id',`cerradas-${ceCount}`);
    cpyEmptyCe.innerHTML = cpyEmptyCe.innerHTML.replace(regex,ceCount);
    totalCeForms.setAttribute('value',ceCount+1);
    
    //apending all elements
    ceTarget.append(cpyEmptyCe);
    // ceTarget.append(btn);
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