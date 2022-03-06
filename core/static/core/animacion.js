const burguerBtn = document.querySelector(".burguer");
const navBtns = document.querySelector(".navButtons");
const usrBtns = document.querySelector(".buttons");

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