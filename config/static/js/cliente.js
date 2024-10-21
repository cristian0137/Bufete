document.addEventListener('DOMContentLoaded',()=>{
    const form = document.getElementById('libro-form')
    const mensaje = document.getElementById('mensaje')

    form.addEventListener('submit',(e)=>{
        e.preventDefault()

        const nombre = document.getElementById('nombre').value
        const apellido = document.getElementById('apellido').value
        const direccion = document.getElementById('direccion').value

        cliente = {nombre,apellido,direccion}

        fetch('/Agregarcliente',{
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify(cliente)
        })
        .then(response =>{
            if(response.status === 201){
                mensaje.textContent = 'Cliente registrado'
                mensaje.style.color = 'blue'
                form.reset()
            }
        })
        .catch(()=>{
            mensaje.textContent = 'Error al registrar al cliente'
            mensaje.style.color = 'red'
        })
    })
})