"""
Blueprint: El Bosque de Pinos — La Tienda.
Un espacio donde los tesoros del bosque esperan ser recolectados.
"""
from flask import Blueprint, render_template
from app.models.bosque import ProductoBosque

bp = Blueprint('bosque', __name__, template_folder='../templates/bosque')


@bp.route('/bosque')
def index():
    """Catálogo de tesoros del bosque."""
    productos = ProductoBosque.query.all()
    return render_template('bosque/index.html', productos=productos)


@bp.route('/bosque/<int:producto_id>')
def producto(producto_id):
    """Detalle de un tesoro."""
    producto = ProductoBosque.query.get_or_404(producto_id)
    return render_template('bosque/producto.html', producto=producto)
