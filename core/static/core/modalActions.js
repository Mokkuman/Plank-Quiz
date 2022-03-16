// checa si existen errores de validación del formulario
// si existen entonces por default se mostrará el modal
if(document.querySelector(".form-errors") != null){
    var myModal = new bootstrap.Modal(document.getElementById('staticBackdropSignin'))
    myModal.show()
}

if(document.querySelector(".errorlist") != null){
    var myModal = new bootstrap.Modal(document.getElementById('staticBackdropSignup'))
    myModal.show()
}