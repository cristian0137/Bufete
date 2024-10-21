from config.database import db



procuradores_expediente = db.Table('procuradores_expediente',
    db.Column('expediente_id', db.Integer, db.ForeignKey('Expedientes.id'), primary_key=True),
    db.Column('procurador_dni', db.Integer, db.ForeignKey('Procuradores.dni'), primary_key=True)
)


class Expediente(db.Model):
    __tablename__ = 'Expedientes'
    id = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=True)
    estado = db.Column(db.String(50), nullable=False)
    cliente_dni = db.Column(db.Integer, db.ForeignKey('Clientes.dni'), nullable=False)

    cliente = db.relationship('Cliente', backref='expedientes')
    procuradores = db.relationship('Procurador', secondary=procuradores_expediente, lazy='subquery', 
                                   backref=db.backref('expedientes', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin,
            'estado': self.estado,
            'cliente': self.cliente.to_dict(),
            'procuradores': [procurador.to_dict() for procurador in self.procuradores]
        }