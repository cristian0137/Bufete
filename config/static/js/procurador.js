document.addEventListener('DOMContentLoaded',()=>{
    const form = document.getElementById('libro-form')
    const mensaje = document.getElementById('mensaje')

    form.addEventListener('submit',(e)=>{
        e.preventDefault()

        const nombre = document.getElementById('nombre').value
        const apellido = document.getElementById('apellido').value
        const direccion = document.getElementById('direccion').value

        procurador = {nombre,apellido,direccion}

        fetch('/Agregarprocurador',{
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify(procurador)
        })
        .then(response =>{
            if(response.status === 201){
                mensaje.textContent = 'Procurador registrado'
                mensaje.style.color = 'blue'
                form.reset()
            }
        })
        .catch(()=>{
            mensaje.textContent = 'Error al registrar al procurador'
            mensaje.style.color = 'red'
        })
    })
})