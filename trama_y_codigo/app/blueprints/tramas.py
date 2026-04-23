"""
Blueprint: Las Tramas — Portafolio de Fibras.
El arte de tejer donde cada hilo cuenta una historia.
"""
from flask import Blueprint, render_template
from app.models.tramas import ProyectoFibras

bp = Blueprint('tramas', __name__, template_folder='../templates/tramas')


@bp.route('/tramas')
def index():
    """Galería de proyectos de fibras — La telaraña del arte."""
    proyectos = ProyectoFibras.query.all()
    return render_template('tramas/index.html', proyectos=proyectos)
