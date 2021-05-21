function validar () {
    // var email = document.getElementsByClassName("email").value;
    // var emailConfirmacao = document.getElementsByClassName("emailConfirm").value;
    var email = cadastro.email.value;
    var emailConfirmacao = cadastro.emailConfirm.value;

    if (email != emailConfirmacao){
        document.getElementById("teste").innerHTML = "Os e-mails não batem!"
        email.focus()
        emailConfirmacao.focus()
        return false
    }
}
