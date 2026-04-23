"""
Modelo: Refugio — El Blog / Bitácora.
Un espacio cálido donde las ideas se guardan junto al fuego.
"""
from datetime import datetime
from app.extensions import db


class EntradaBitacora(db.Model):
    __tablename__ = 'bitacora_refugio'

    id = db.Column(db.Integer, primary_key=True)
    titulo_entrada = db.Column(db.String(200), nullable=False)
    contenido_calido = db.Column(db.Text)
    humor_del_dia = db.Column(db.String(50))
    imagen_url = db.Column(db.String(255))
    fecha_publicacion = db.Column(db.Date, default=datetime.utcnow)

    # Relación con comentarios
    comentarios = db.relationship('Comentario', backref='entrada', lazy='dynamic')

    def __repr__(self):
        return f'<Bitácora: {self.titulo_entrada}>'


class Comentario(db.Model):
    __tablename__ = 'comentarios'

    id = db.Column(db.Integer, primary_key=True)
    articulo_id = db.Column(db.Integer, db.ForeignKey('bitacora_refugio.id', ondelete='CASCADE'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete='CASCADE'))
    contenido = db.Column(db.Text, nullable=False)
    fecha_comentario = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Comentario de {self.usuario_id} en {self.articulo_id}>'
