from flask import request,jsonify,render_template,Blueprint
from config.database import db,app
from models.Model_cliente import Cliente
from models.Model_procurador import Procurador
from models.Model_Expediente import Expediente

db.init_app(app)

with app.app_context():
    db.create_all()



#prueba---------------------------------------------------------

@app.route('/expedientes', methods=['POST'])
def agregar_expediente():
    # Obtener datos del formulario
    data = request.get_json()
    
    print(data)
    # Validar que los datos estén presentes
    if  data.get('cliente_dni') is None or  data.get('procuradores_ids') is None or data.get('fecha_inicio') is None or  data.get('estado') is None:
        return jsonify({'error': 'Faltan datos'}), 400
 
    # Buscar el cliente
    cliente = Cliente.query.get(data.get('cliente_dni'))
    if not cliente:
        return jsonify({'error': 'Cliente no encontrado'}), 404

    # Crear un nuevo expediente
    nuevo_expediente = Expediente(fecha_inicio=data.get('fecha_inicio'), fecha_fin=data.get('fecha_fin'), estado=data.get('estado'), cliente_dni=cliente.dni)
    #print(nuevo_expediente)
    # Agregar procuradores al expediente
    for procurador_id in data.get('procuradores_ids'):
        procurador = Procurador.query.get(procurador_id)
        if procurador:
            nuevo_expediente.procuradores.append(procurador)

    # Guardar en la base de datos
    db.session.add(nuevo_expediente)
    db.session.commit()

    return jsonify({'message': 'Expediente creado exitosamente'}), 201

#----------------------------------------------------------------------------
# rutas
@app.route('/')
def index():
    return 'Hola'

@app.route('/r_cliente')
def registrar_clientes():
    return render_template('clientes.html')

@app.route('/r_procurador')
def registrar_procuradores():
    return render_template('procuradores.html')

@app.route('/r_expediente')
def registrar_expediente():
    return render_template('expediente.html')


# Metodos POST

@app.route('/Agregarcliente',methods = ['POST'])
def Agregar_cliente():
    data = request.get_json()
    nuevo_cliente = Cliente(
        nombre = data.get('nombre'),
        apellido = data.get('apellido'),
        direccion = data.get('direccion')
    )
    db.session.add(nuevo_cliente)
    db.session.commit()
    return 'Cliente guardado',201


@app.route('/Agregarprocurador',methods = ['POST'])
def Agregar_procurador():
    data = request.get_json()
    nuevo_procurador = Procurador(
        nombre =  data.get('nombre'),
        apellido =  data.get('apellido'),
        direccion =  data.get('direccion')
    )
    db.session.add(nuevo_procurador)
    db.session.commit()
    return 'Procurador guardado',201








if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

