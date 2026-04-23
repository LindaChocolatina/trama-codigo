"""
Modelo: Usuario — Los visitantes y guardianes del jardín.

Roles:
  - administradora: La Jardinera. Planta, poda y cuida el ecosistema.
  - cliente: El caminante. Explora, lee y recolecta tesoros.
"""
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.extensions import db, login_manager


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(20), default='cliente')  # 'administradora' o 'cliente'
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    # Relaciones — Las raíces que conectan al usuario con el jardín
    comentarios = db.relationship('Comentario', backref='autor', lazy='dynamic')
    items_canasto = db.relationship('CarritoMimbre', backref='caminante', lazy='dynamic')
    pedidos = db.relationship('Pedido', backref='comprador', lazy='dynamic')

    def plantar_contrasena(self, contrasena):
        """Siembra una contraseña segura en la tierra del usuario."""
        self.password_hash = generate_password_hash(contrasena)

    def verificar_contrasena(self, contrasena):
        """Verifica si la semilla coincide con la planta."""
        return check_password_hash(self.password_hash, contrasena)

    @property
    def es_jardinera(self):
        """¿Es esta persona la guardiana del jardín?"""
        return self.rol == 'administradora'

    def __repr__(self):
        return f'<Usuario {self.username} ({self.rol})>'


@login_manager.user_loader
def cargar_usuario(user_id):
    """El portón reconoce al visitante por su identificación."""
    return Usuario.query.get(int(user_id))
