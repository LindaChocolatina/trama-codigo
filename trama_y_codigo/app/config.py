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


class DesarrolloConfig(Config):
    """Primavera — Donde todo brota y se experimenta."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///jardin_interactivo.db'
    )


class ProduccionConfig(Config):
    """Verano — El jardín en plena floración."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


# Mapa de estaciones
configuraciones = {
    'desarrollo': DesarrolloConfig,
    'produccion': ProduccionConfig,
    'default': DesarrolloConfig
}
