"""
Modelo: Canasto de Mimbre — El carrito de compras artesanal.
Cada tesoro recolectado se guarda en un canasto tejido a mano.
"""
from datetime import datetime
from app.extensions import db


class CarritoMimbre(db.Model):
    __tablename__ = 'carrito_mimbre'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete='CASCADE'))
    producto_id = db.Column(db.Integer, db.ForeignKey('inventario_bosque.id', ondelete='CASCADE'))
    cantidad = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f'<Canasto: {self.cantidad}x producto {self.producto_id}>'


class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    total = db.Column(db.Numeric(10, 2), nullable=False)
    metodo_pago = db.Column(db.String(20))  # 'paypal', 'nequi', 'transferencia'
    estado_pago = db.Column(db.String(20), default='pendiente')  # 'pendiente', 'completado', 'fallido'
    referencia_pago = db.Column(db.String(100))
    comprobante_url = db.Column(db.String(255))
    fecha_pedido = db.Column(db.DateTime, default=datetime.utcnow)
    
    detalles = db.relationship('DetallePedido', backref='pedido', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Pedido #{self.id} — {self.estado_pago}>'

class DetallePedido(db.Model):
    __tablename__ = 'detalle_pedido'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id', ondelete='CASCADE'))
    producto_id = db.Column(db.Integer, db.ForeignKey('inventario_bosque.id'))
    cantidad = db.Column(db.Integer, nullable=False, default=1)
    precio_unitario = db.Column(db.Numeric(10, 2), nullable=False)

    producto = db.relationship('ProductoBosque')

    def __repr__(self):
        return f'<DetallePedido Pedido={self.pedido_id} Prod={self.producto_id}>'
