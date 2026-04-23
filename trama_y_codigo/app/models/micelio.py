"""
Modelo: Micelio — La red de contacto.
Como los hongos conectan el bosque bajo tierra,
esta sección gestiona las conexiones humanas.
"""
from datetime import datetime
from app.extensions import db


class ConexionMicelio(db.Model):
    __tablename__ = 'conexiones_micelio'

    id = db.Column(db.Integer, primary_key=True)
    nombre_visitante = db.Column(db.String(100), nullable=False)
    mensaje_raiz = db.Column(db.Text, nullable=False)
    email_contacto = db.Column(db.String(150), nullable=False)
    fecha_conexion = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Conexión: {self.nombre_visitante} — {self.fecha_conexion}>'
