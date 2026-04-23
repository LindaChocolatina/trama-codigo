"""
Blueprint: El Canasto de Mimbre — Carrito de Compras.
Los tesoros recolectados esperan en un canasto tejido a mano.
"""
from flask import Blueprint, render_template, session, redirect, url_for, request, flash, jsonify

bp = Blueprint('canasto', __name__, template_folder='../templates/canasto')


def obtener_canasto():
    """Obtiene el canasto de la sesión actual."""
    if 'canasto' not in session:
        session['canasto'] = []
    return session['canasto']


@bp.route('/canasto')
def index():
    """Vista del canasto de mimbre."""
    canasto = obtener_canasto()
    return render_template('canasto/index.html', canasto=canasto)


@bp.route('/canasto/agregar/<int:producto_id>', methods=['POST'])
def agregar(producto_id):
    """Agrega un tesoro al canasto."""
    from app.models.bosque import ProductoBosque
    producto = ProductoBosque.query.get_or_404(producto_id)

    canasto = obtener_canasto()
    # Verificar si ya está en el canasto
    for item in canasto:
        if item['id'] == producto_id:
            item['cantidad'] += 1
            session.modified = True
            flash(f'Otro {producto.producto} cae suavemente en tu canasto.', 'exito')
            return redirect(url_for('bosque.index'))

    canasto.append({
        'id': producto_id,
        'nombre': producto.producto,
        'precio': float(producto.precio),
        'cantidad': 1
    })
    session.modified = True
    flash(f'{producto.producto} ha sido recolectado en tu canasto de mimbre.', 'exito')
    return redirect(url_for('bosque.index'))


@bp.route('/canasto/quitar/<int:producto_id>', methods=['POST'])
def quitar(producto_id):
    """Devuelve un tesoro al bosque."""
    canasto = obtener_canasto()
    session['canasto'] = [item for item in canasto if item['id'] != producto_id]
    session.modified = True
    flash('El tesoro ha vuelto al bosque.', 'info')
    return redirect(url_for('canasto.index'))
