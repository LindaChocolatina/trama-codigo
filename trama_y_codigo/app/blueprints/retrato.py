"""
Blueprint: El Retrato — Sobre Mí.
La sección biográfica que humaniza la marca.
De día, la mujer camina por el jardín. De noche, su luz brilla en la ventana.
"""
from flask import Blueprint, render_template
from app.services.reloj_logico import obtener_estado_mundo

bp = Blueprint('retrato', __name__, template_folder='../templates/retrato')


@bp.route('/retrato')
def index():
    """Página 'Sobre mí' — El retrato de la jardinera."""
    estado = obtener_estado_mundo()
    return render_template('retrato/index.html', estado=estado)
