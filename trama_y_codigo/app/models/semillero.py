"""
Modelo: Semillero — Proyectos de Software.
Cada flor es un proyecto que brotó de una semilla de código.
"""
from datetime import datetime
from app.extensions import db


class ProyectoSoftware(db.Model):
    __tablename__ = 'proyectos_software'

    id = db.Column(db.Integer, primary_key=True)
    nombre_flor = db.Column(db.String(100))  # Atributo poético
    titulo = db.Column(db.String(150), nullable=False)
    stack_tecnico = db.Column(db.String(200))
    descripcion_logica = db.Column(db.Text)
    repo_url = db.Column(db.String(255))
    imagen_url = db.Column(db.String(255))
    fecha_brote = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Flor: {self.nombre_flor} — {self.titulo}>'
