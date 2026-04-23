"""
Blueprint: El Canasto de Mimbre — Carrito de Compras y Checkout.
Los tesoros recolectados esperan en un canasto tejido a mano para ser llevados a casa.
"""
import os
from flask import Blueprint, render_template, session, redirect, url_for, request, flash, jsonify, current_app
from werkzeug.utils import secure_filename
from app.extensions import db
from app.models.bosque import ProductoBosque
from app.models.canasto import Pedido, DetallePedido
from app.models.usuario import Usuario

bp = Blueprint('canasto', __name__, template_folder='../templates/canasto')


def obtener_canasto():
    """Obtiene el canasto de la sesión actual."""
    if 'canasto' not in session:
        session['canasto'] = []
    return session['canasto']


def calcular_total_canasto():
    """Calcula el valor total del canasto."""
    canasto = obtener_canasto()
    return sum(item['precio'] * item['cantidad'] for item in canasto)


@bp.route('/canasto')
def index():
    """Vista del canasto de mimbre."""
    canasto = obtener_canasto()
    return render_template('canasto/index.html', canasto=canasto)


@bp.route('/canasto/agregar/<int:producto_id>', methods=['POST'])
def agregar(producto_id):
    """Agrega un tesoro al canasto."""
    producto = ProductoBosque.query.get_or_404(producto_id)

    if producto.stock_disponible <= 0:
        flash(f'El tesoro "{producto.producto}" se ha agotado en el bosque.', 'error')
        return redirect(url_for('bosque.index'))

    canasto = obtener_canasto()
    # Verificar si ya está en el canasto
    for item in canasto:
        if item['id'] == producto_id:
            if item['cantidad'] >= producto.stock_disponible:
                flash(f'No hay suficientes "{producto.producto}" en el bosque.', 'error')
                return redirect(url_for('canasto.index'))
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


@bp.route('/canasto/checkout', methods=['GET', 'POST'])
def checkout():
    """Paso 1: Identificarse como invitado para llevar los tesoros."""
    canasto = obtener_canasto()
    if not canasto:
        flash('Tu canasto está vacío. No hay nada que llevar a casa.', 'error')
        return redirect(url_for('bosque.index'))

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip()

        # Buscar si el usuario ya existe, si no, crear un "invitado" (cliente)
        usuario = Usuario.query.filter_by(email=email).first()
        if not usuario:
            usuario = Usuario(username=nombre, email=email, rol='cliente')
            db.session.add(usuario)
            db.session.commit()

        # Crear el pedido
        total = calcular_total_canasto()
        pedido = Pedido(usuario_id=usuario.id, total=total, estado_pago='pendiente')
        db.session.add(pedido)
        db.session.commit()

        # Añadir los detalles del pedido
        for item in canasto:
            detalle = DetallePedido(
                pedido_id=pedido.id,
                producto_id=item['id'],
                cantidad=item['cantidad'],
                precio_unitario=item['precio']
            )
            db.session.add(detalle)
        
        db.session.commit()
        return redirect(url_for('canasto.pago', pedido_id=pedido.id))

    return render_template('canasto/checkout.html', canasto=canasto, total=calcular_total_canasto())


@bp.route('/canasto/pago/<int:pedido_id>')
def pago(pedido_id):
    """Paso 2: Elegir el camino del pago (Nequi o PayPal)."""
    pedido = Pedido.query.get_or_404(pedido_id)
    if pedido.estado_pago == 'completado':
        flash('Estos tesoros ya han sido intercambiados.', 'info')
        return redirect(url_for('canasto.index'))
    
    return render_template('canasto/pago.html', pedido=pedido, paypal_client_id=current_app.config['PAYPAL_CLIENT_ID'])


@bp.route('/canasto/confirmar-nequi', methods=['POST'])
def confirmar_nequi():
    """Paso 3a: La carta con el comprobante de Nequi llega a la jardinera."""
    pedido_id = request.form.get('pedido_id')
    pedido = Pedido.query.get_or_404(pedido_id)

    if 'comprobante' not in request.files:
        flash('No has adjuntado el comprobante en tu carta.', 'error')
        return redirect(url_for('canasto.pago', pedido_id=pedido.id))
    
    file = request.files['comprobante']
    if file.filename == '':
        flash('La carta estaba vacía. Selecciona una imagen.', 'error')
        return redirect(url_for('canasto.pago', pedido_id=pedido.id))

    if file:
        filename = secure_filename(f"nequi_pedido_{pedido.id}_{file.filename}")
        upload_path = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_path, exist_ok=True)
        file.save(os.path.join(upload_path, filename))

        pedido.metodo_pago = 'nequi'
        pedido.comprobante_url = filename
        pedido.estado_pago = 'pendiente' # La jardinera debe verificarlo
        
        # Restar el stock
        for detalle in pedido.detalles:
            if detalle.producto.stock_disponible > 0:
                detalle.producto.stock_disponible -= detalle.cantidad

        # Limpiar canasto
        session['canasto'] = []
        db.session.commit()

        return redirect(url_for('canasto.gracias', metodo='nequi'))


@bp.route('/canasto/confirmar-paypal', methods=['POST'])
def confirmar_paypal():
    """Paso 3b: El pago mágico instantáneo de PayPal."""
    data = request.get_json()
    pedido_id = data.get('pedido_id')
    transaction_id = data.get('transaction_id')

    pedido = Pedido.query.get_or_404(pedido_id)
    pedido.metodo_pago = 'paypal'
    pedido.referencia_pago = transaction_id
    pedido.estado_pago = 'completado'

    # Restar el stock
    for detalle in pedido.detalles:
        if detalle.producto.stock_disponible > 0:
            detalle.producto.stock_disponible -= detalle.cantidad

    # Limpiar canasto
    session['canasto'] = []
    db.session.commit()

    return jsonify({'success': True, 'url': url_for('canasto.gracias', metodo='paypal')})


@bp.route('/canasto/gracias')
def gracias():
    """El fin del intercambio. Un agradecimiento narrativo."""
    metodo = request.args.get('metodo', 'desconocido')
    return render_template('canasto/gracias.html', metodo=metodo)
