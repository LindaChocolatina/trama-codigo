"""
Modelo: Tramas — Proyectos de Fibras y Tejido.
Cada hilo es una historia que conecta lo analógico con lo digital.
"""
from app.extensions import db


class ProyectoFibras(db.Model):
    __tablename__ = 'proyectos_fibras'

    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(100))
    tecnica_tejido = db.Column(db.String(100))
    titulo_pieza = db.Column(db.String(150))
    historia_trama = db.Column(db.Text)
    imagen_url = db.Column(db.String(255))

    def __repr__(self):
        return f'<Trama: {self.titulo_pieza} ({self.tecnica_tejido})>'
