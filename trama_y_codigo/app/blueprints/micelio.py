"""
Blueprint: El Micelio — Contacto.
La red invisible que conecta al bosque por debajo de la tierra.
"""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.extensions import db
from app.models.micelio import ConexionMicelio

bp = Blueprint('micelio', __name__, template_folder='../templates/micelio')


@bp.route('/micelio', methods=['GET', 'POST'])
def index():
    """Formulario de contacto — Enviar una raíz al micelio."""
    if request.method == 'POST':
        conexion = ConexionMicelio(
            nombre_visitante=request.form.get('nombre', '').strip(),
            mensaje_raiz=request.form.get('mensaje', '').strip(),
            email_contacto=request.form.get('email', '').strip()
        )
        db.session.add(conexion)
        db.session.commit()
        flash('Tu mensaje ha echado raíces en el micelio. Pronto brotará una respuesta.', 'exito')
        return redirect(url_for('micelio.index'))

    return render_template('micelio/index.html')
