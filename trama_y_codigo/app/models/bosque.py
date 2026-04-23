"""
Modelo: Bosque de Pinos — El inventario de la Tienda.
Los tesoros del bosque esperan ser recolectados.
"""
from app.extensions import db


class ProductoBosque(db.Model):
    __tablename__ = 'inventario_bosque'

    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(150), nullable=False)
    precio = db.Column(db.Numeric(10, 2))
    categoria = db.Column(db.String(20))  # 'digital' o 'fisico'
    stock_disponible = db.Column(db.Integer, default=0)
    imagen_url = db.Column(db.String(255))
    descripcion = db.Column(db.Text)

    # Relación con el canasto
    items_canasto = db.relationship('CarritoMimbre', backref='tesoro', lazy='dynamic')

    def __repr__(self):
        return f'<Tesoro: {self.producto} — ${self.precio}>'
