"""
Blueprint: El Semillero — Portafolio de Software.
Cada flor es un proyecto que brotó de una semilla de código.
"""
from flask import Blueprint, render_template
from app.models.semillero import ProyectoSoftware

bp = Blueprint('semillero', __name__, template_folder='../templates/semillero')


@bp.route('/semillero')
def index():
    """Galería de proyectos de software — Las flores del jardín."""
    proyectos = ProyectoSoftware.query.order_by(
        ProyectoSoftware.fecha_brote.desc()
    ).all()
    return render_template('semillero/index.html', proyectos=proyectos)
