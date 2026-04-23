"""
Blueprint: La Jardinera — Panel de Administración.
Solo la guardiana del jardín puede plantar, podar y cuidar el ecosistema.
"""
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.extensions import db
from app.models.usuario import Usuario

bp = Blueprint('jardinera', __name__, template_folder='../templates/jardinera')


@bp.route('/jardinera/login', methods=['GET', 'POST'])
def login():
    """La puerta del jardín — Identificarse como jardinera."""
    if current_user.is_authenticated:
        return redirect(url_for('jardinera.dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        contrasena = request.form.get('contrasena', '')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.verificar_contrasena(contrasena):
            login_user(usuario)
            flash('Bienvenida de vuelta al jardín.', 'exito')
            return redirect(url_for('jardinera.dashboard'))
        flash('Las credenciales no coinciden con ninguna semilla plantada.', 'error')

    return render_template('jardinera/login.html')


@bp.route('/jardinera/logout')
@login_required
def logout():
    """Cerrar el portón del jardín."""
    logout_user()
    flash('Has dejado el jardín. Vuelve pronto.', 'info')
    return redirect(url_for('jardin.escena'))


@bp.route('/jardinera')
@login_required
def dashboard():
    """Panel de la jardinera — Vista general del ecosistema."""
    if not current_user.es_jardinera:
        flash('Solo la jardinera puede acceder a este rincón.', 'error')
        return redirect(url_for('jardin.escena'))

    from app.models import (
        ProyectoSoftware, ProyectoFibras,
        EntradaBitacora, ProductoBosque, ConexionMicelio
    )
    stats = {
        'flores': ProyectoSoftware.query.count(),
        'tramas': ProyectoFibras.query.count(),
        'entradas': EntradaBitacora.query.count(),
        'tesoros': ProductoBosque.query.count(),
        'conexiones': ConexionMicelio.query.count(),
    }
    return render_template('jardinera/dashboard.html', stats=stats)
