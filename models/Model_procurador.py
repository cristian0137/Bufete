from config.database import db



class Procurador(db.Model):

    __tablename__ = 'Procuradores'
    dni = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    
    

    def to_dict (self):
        return{
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'direccion': self.direccion,
        }