"""
Configuraciones del Jardín Interactivo.
Cada entorno es una estación del año en el ciclo de desarrollo.
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuración base — La semilla de todo jardín."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'semilla-secreta-por-defecto')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max para uploads
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads', 'comprobantes')
    PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID', 'test')


class DesarrolloConfig(Config):
    """Primavera — Donde todo brota y se experimenta."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///jardin_interactivo.db'
    )


class ProduccionConfig(Config):
    """Verano — El jardín en plena floración."""
    DEBUG = False
    _uri = os.environ.get('DATABASE_URL')
    if _uri and _uri.startswith("postgres://"):
        _uri = _uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = _uri


# Mapa de estaciones
configuraciones = {
    'desarrollo': DesarrolloConfig,
    'produccion': ProduccionConfig,
    'development': DesarrolloConfig,
    'testing': DesarrolloConfig,
    'default': DesarrolloConfig
}
