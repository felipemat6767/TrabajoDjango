document.getElementById('formInf').addEventListener('submit', function(event) { 
    const nombre = document.getElementById('fname');
    const email = document.getElementById('lemail');
    const contraseña = document.getElementById('password');   
    if (nombre.value === '') {
        alert("Escribir un nombre valido")
        nombre.parentNode.classList.add('error');
        nombre.parentNode.classList.remove('success');
        mensajeExito += "Escribir un nombre valido"
    } else { 
      nombre.parentNode.classList.add('success');
      nombre.parentNode.classList.remove('error');
    }

        //Validacion de Email
    if (email.value === '') {
        alert("Escribir un email valido")
        nombre.parentNode.classList.add('error');
        nombre.parentNode.classList.remove('success');
    } else if ( !email.value.match(mailFormato)) {
        alert("Escribir un email valido")
        emailInput.parentNode.classList.add('error');
        emailInput.parentNode.classList.remove('success');
    }
      else { 
      nombre.parentNode.classList.add('success');
      nombre.parentNode.classList.remove('error');
    }
            //Validacion de Contraseña

    if (contraseña.value === '' || contraseña.value.length > 18 || contraseña.value.length <= 6) { 
        alert("Escribir una contraseña valida")
        nombre.parentNode.classList.add('error');
        nombre.parentNode.classList.remove('success');
    } else if (!contraseña.value.match(contraseñaFormato)) {
        alert("Escribir una contraseña valida")
        emailInput.parentNode.classList.add('error');
        emailInput.parentNode.classList.remove('success');
    }
      else { 
      nombre.parentNode.classList.add('success');
      nombre.parentNode.classList.remove('error');
    }    
});