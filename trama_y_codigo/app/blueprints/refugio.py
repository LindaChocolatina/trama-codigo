"""
Blueprint: El Refugio — El Blog.
Un espacio de introspección junto al fuego de la chimenea.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from app.models.refugio import EntradaBitacora, Comentario
from app.extensions import db
from app.forms import ComentarioForm

bp = Blueprint('refugio', __name__, template_folder='../templates/refugio')


@bp.route('/refugio')
def index():
    """Listado de entradas de la bitácora."""
    entradas = EntradaBitacora.query.order_by(
        EntradaBitacora.fecha_publicacion.desc()
    ).all()
    return render_template('refugio/index.html', entradas=entradas)


@bp.route('/refugio/<int:entrada_id>', methods=['GET', 'POST'])
def entrada(entrada_id):
    """Detalle de una entrada del blog y comentarios."""
    entrada_obj = EntradaBitacora.query.get_or_404(entrada_id)
    form = ComentarioForm()
    
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('Debes ingresar para dejar tus huellas.', 'error')
            return redirect(url_for('auth.login', next=request.url))
            
        comentario = Comentario(
            articulo_id=entrada_obj.id,
            usuario_id=current_user.id,
            contenido=form.contenido.data
        )
        db.session.add(comentario)
        db.session.commit()
        flash('Has dejado tus huellas en este refugio.', 'exito')
        return redirect(url_for('refugio.entrada', entrada_id=entrada_obj.id))
        
    return render_template('refugio/entrada.html', entrada=entrada_obj, form=form)
