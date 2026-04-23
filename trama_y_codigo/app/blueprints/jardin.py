"""
Blueprint: El Jardín — La escena principal.
La puerta de entrada al ecosistema, donde el paisaje cobra vida.
"""
from flask import Blueprint, render_template, jsonify
from app.services.reloj_logico import obtener_estado_mundo, obtener_saludo

bp = Blueprint('jardin', __name__, template_folder='../templates/jardin')


@bp.route('/')
def escena():
    """Renderiza la escena principal del jardín interactivo."""
    estado = obtener_estado_mundo()
    saludo = obtener_saludo()
    return render_template(
        'jardin/escena.html',
        estado=estado,
        saludo=saludo
    )


@bp.route('/api/estado-mundo')
def api_estado_mundo():
    """API endpoint para que el frontend consulte el estado del tiempo."""
    estado = obtener_estado_mundo()
    return jsonify(estado)
