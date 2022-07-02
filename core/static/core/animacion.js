const burguerBtn = document.querySelector(".burguer");
const navBtns = document.querySelector(".navButtons");
const usrBtns = document.querySelector(".buttons");
/*animacion NuevaPractica */
const addBtn = document.querySelector(".addBtn");
const btnWrapper = document.querySelector(".btnWrapper");


burguerBtn.addEventListener("click", () => {
    //animacion burguer btn
    animacion();
    navBtns.classList.toggle("activado");
    
});
function animacion(){
    usrBtns.classList.toggle("abrir");
    burguerBtn.querySelectorAll("span").forEach(
        (span)=> span.classList.toggle("abrir"));
}
/*animacion NuevaPractica */
addBtn.addEventListener("click", ()=> {
    //btnWrapper.classList.toggle("open");
    //console.log("xd, pulsado el btnAdd");
    btnWrapper.querySelectorAll("button").forEach((button)=>{
        button.classList.toggle("open");
    })
});