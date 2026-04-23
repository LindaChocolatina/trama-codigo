"""
Blueprint: El Refugio — El Blog.
Un espacio de introspección junto al fuego de la chimenea.
"""
from flask import Blueprint, render_template
from app.models.refugio import EntradaBitacora

bp = Blueprint('refugio', __name__, template_folder='../templates/refugio')


@bp.route('/refugio')
def index():
    """Listado de entradas de la bitácora."""
    entradas = EntradaBitacora.query.order_by(
        EntradaBitacora.fecha_publicacion.desc()
    ).all()
    return render_template('refugio/index.html', entradas=entradas)


@bp.route('/refugio/<int:entrada_id>')
def entrada(entrada_id):
    """Detalle de una entrada del blog."""
    entrada = EntradaBitacora.query.get_or_404(entrada_id)
    return render_template('refugio/entrada.html', entrada=entrada)
