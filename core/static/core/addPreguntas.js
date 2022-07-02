//variables contadoras para agregar a mi formulario
let ab = 1; //contador pregunta abierta
let ce = 1; //contador pregunta cerrada
const LIMITE_OPCIONES = 6;

const addPregAbierta = document.querySelector(".addPregAbierta");
const addPregCerrada = document.querySelector(".addPregCerrada");
const divPregunta = document.querySelector(".Preguntas");//Padre

function createPregAbierta(){
    const divAbierta = document.createElement("div");
    divAbierta.setAttribute('class',"pregAbierta-"+ab);

    const pregAb = document.createElement("input"); //planteamiento
    pregAb.placeholder="Pregunta";
    pregAb.setAttribute('type',"text");

    const respAb = document.createElement("input"); //respuesta
    respAb.placeholder ="Respuesta";
    respAb.setAttribute('type',"text");

    //append a divAbierta
    divAbierta.appendChild(pregAb); divAbierta.appendChild(respAb);

    divPregunta.appendChild(divAbierta);//append al parent form
    ab++;
}
//contOpcion = contador de opciones creadas, parent = div parent al que se va a attach
function createResp(contOpcion,parent){
    const respCe = document.createElement("input");
    respCe.placeholder="Opcion "+contOpcion;
    respCe.setAttribute('type',"text");
    parent.appendChild(respCe);
    console.log("opcion dentro de createResp "+contOpcion);
}

function createPregCerrada(){
    let opcion = 1; //contador opciones

    //div contenedor de la pregunta cerrada
    const divCerrada = document.createElement("div");
    divCerrada.setAttribute('class',"pregCerrada-"+ce);

    const pregCe = document.createElement("input"); 
    pregCe.placeholder="Pregunta";
    pregCe.setAttribute('type',"text");

    //div cerrada es la que crece por las opciones
    const divResp = document.createElement("div");
    divResp.setAttribute('class',"respuestas");

    //createResp(opcion,divResp); //creando respuesta inicial
    const respCe = document.createElement("input");
    respCe.placeholder="Opcion "+opcion;
    respCe.setAttribute('type',"text");

    let addRespBtn = document.createElement("button");
    addRespBtn.setAttribute('id',"opcion"+opcion);
    addRespBtn.setAttribute('type',"button");
    addRespBtn.innerHTML = "Añadir opcion";
    //append al divResp este tiene las opciones de una pregunta cerrada
    
    divResp.appendChild(respCe); //añadiendo respuesta inicial
    //divResp.appendChild(addRespBtn); //adñadiendo boton añadir opcion

    //onclick event al boton para añadir una nueva opcion
    addRespBtn.addEventListener("click",() =>{
        opcion++;
        //while(opcion < LIMITE_OPCIONES){ 
            const addOpc = document.createElement("input");
            addOpc.placeholder="Opcion "+opcion;
            addOpc.setAttribute('type',"text");
            divResp.appendChild(addOpc);
            console.log("opcion dentro de createResp "+opcion);
            //opcion++;
        //}
    });

    console.log("opcion dentro de createPregCerrada "+opcion);

    divCerrada.appendChild(pregCe); //añadiendo planteamiento
    divCerrada.appendChild(divResp);
    divCerrada.appendChild(addRespBtn);

    divPregunta.appendChild(divCerrada);//append al parent form

    ce++; //aumentando contador
}


//EVENT LISTENERS
addPregAbierta.addEventListener("click",()=>{
    // console.log("Añadiendo una pregunta ABIERTA");
    createPregAbierta();
});

addPregCerrada.addEventListener("click",()=>{
    // console.log("Añadiendo una pregunta CERRADA");
    createPregCerrada();
});