// checa si existen errores de validación del formulario
// si existen entonces por default se mostrará el modal

var ready = (callback) => {
    if (document.readyState != "loading") callback();
    else document.addEventListener("DOMContentLoaded", callback);
  }
  
ready(() => { 
    if(document.querySelector(".form-errors") != null || window.location.href.includes('signin?')){
        var myModal = new bootstrap.Modal(document.getElementById('staticBackdropSignin'));
        myModal.show();
    }
    
    if(document.querySelector(".errorlist") != null || document.querySelector(".invalid-feedback") != null){
        var myModal = new bootstrap.Modal(document.getElementById('staticBackdropSignup'));
        myModal.show();
    }
});