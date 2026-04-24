"""
Extensiones del ecosistema — Las raíces compartidas del jardín.
Cada extensión es una raíz que alimenta múltiples partes de la aplicación.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

# La tierra fértil donde crecen los modelos
db = SQLAlchemy()

# El guardián del portón — controla quién entra al jardín
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Debes identificarte para entrar a este rincón del jardín.'
login_manager.login_message_category = 'info'

# El escudo protector contra visitantes malintencionados
csrf = CSRFProtect()
