"""
Blueprint: Autenticación — La Puerta al Ecosistema.
Donde los visitantes se convierten en parte de la comunidad.
"""
from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models.usuario import Usuario
from app.forms import LoginForm, RegistroForm
from datetime import datetime
import os

bp = Blueprint('auth', __name__, template_folder='../templates/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """La puerta del jardín — Identificarse en la comunidad."""
    if current_user.is_authenticated:
        if current_user.es_jardinera:
            return redirect(url_for('jardinera.dashboard'))
        return redirect(url_for('jardin.escena'))

    form = LoginForm()
    if form.validate_on_submit():
        try:
            usuario = Usuario.query.filter_by(email=form.email.data).first()
            if usuario and usuario.verificar_contrasena(form.contrasena.data):
                login_user(usuario)
                if usuario.es_jardinera:
                    flash('Bienvenida de vuelta al panel de control.', 'exito')
                    return redirect(url_for('jardinera.dashboard'))
                else:
                    flash(f'Bienvenido al refugio, {usuario.username}.', 'exito')
                    next_page = request.args.get('next')
                    return redirect(next_page or url_for('jardin.escena'))
            
            flash('Las credenciales no coinciden con ninguna semilla plantada en el jardín.', 'error')
        except Exception as e:
            import traceback
            log_path = os.path.join(current_app.root_path, 'error_log.txt')
            with open(log_path, 'a') as f:
                f.write(f"\n--- ERROR LOGIN at {datetime.now()} ---\n")
                f.write(traceback.format_exc())
            flash('Error interno al intentar ingresar. El detalle se ha registrado.', 'error')
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html', form=form)


@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    """Unirse a la comunidad de Trama & Código."""
    if current_user.is_authenticated:
        return redirect(url_for('jardin.escena'))

    form = RegistroForm()
    if form.validate_on_submit():
        try:
            # Verificar si el correo ya existe
            if Usuario.query.filter_by(email=form.email.data).first():
                flash('Este correo mágico ya está registrado en el bosque.', 'error')
                return redirect(url_for('auth.registro'))
            
            # Verificar si el apodo ya existe
            if Usuario.query.filter_by(username=form.username.data).first():
                flash('Este apodo ya ha sido tomado por otro caminante.', 'error')
                return redirect(url_for('auth.registro'))

            nuevo_usuario = Usuario(
                username=form.username.data,
                email=form.email.data,
                rol='cliente'
            )
            nuevo_usuario.plantar_contrasena(form.contrasena.data)
            db.session.add(nuevo_usuario)
            db.session.commit()

            login_user(nuevo_usuario)
            flash('¡Tu semilla ha sido plantada! Bienvenido a la comunidad.', 'exito')
            return redirect(url_for('jardin.escena'))
        except Exception as e:
            import traceback
            log_path = os.path.join(current_app.root_path, 'error_log.txt')
            with open(log_path, 'a') as f:
                f.write(f"\n--- ERROR REGISTRO at {datetime.now()} ---\n")
                f.write(traceback.format_exc())
            db.session.rollback()
            flash('Hubo un problema al plantar tu semilla. El detalle se ha registrado.', 'error')
            return redirect(url_for('auth.registro'))

    return render_template('auth/registro.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    """Cerrar el portón y dejar el jardín."""
    logout_user()
    flash('Has dejado el jardín. Vuelve pronto.', 'info')
    return redirect(url_for('jardin.escena'))
