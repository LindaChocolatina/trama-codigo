"""
Formularios del Panel Administrativo (WTForms).
Donde se validan las semillas antes de plantarlas en la base de datos.
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, DecimalField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class FlorForm(FlaskForm):
    """Formulario para Proyectos de Software (Semillero)."""
    nombre_flor = StringField('Nombre Poético (Ej. Lupino Azul)', validators=[Optional(), Length(max=100)])
    titulo = StringField('Título del Proyecto', validators=[DataRequired(), Length(max=150)])
    stack_tecnico = StringField('Stack Técnico (Ej. Python, Flask, React)', validators=[Optional(), Length(max=200)])
    descripcion_logica = TextAreaField('Descripción Lógica', validators=[Optional()])
    repo_url = StringField('URL del Repositorio', validators=[Optional(), Length(max=255)])
    imagen = FileField('Imagen de Portada', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'webp'], 'Solo se permiten imágenes.')])
    submit = SubmitField('Plantar Flor')


class TramaForm(FlaskForm):
    """Formulario para Proyectos de Fibra (Tramas)."""
    titulo_pieza = StringField('Título de la Pieza', validators=[DataRequired(), Length(max=150)])
    material = StringField('Material (Ej. Lana merino, Algodón)', validators=[Optional(), Length(max=100)])
    tecnica_tejido = StringField('Técnica (Ej. Crochet, Macramé)', validators=[Optional(), Length(max=100)])
    historia_trama = TextAreaField('Historia de la Pieza', validators=[Optional()])
    imagen = FileField('Imagen de Portada', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'webp'], 'Solo se permiten imágenes.')])
    submit = SubmitField('Tejer Trama')


class BitacoraForm(FlaskForm):
    """Formulario para el Blog (Refugio)."""
    titulo_entrada = StringField('Título de la Entrada', validators=[DataRequired(), Length(max=150)])
    humor_del_dia = StringField('Humor del Día (Ej. Inspirada, Reflexiva)', validators=[Optional(), Length(max=50)])
    contenido_calido = TextAreaField('Contenido del Texto', validators=[DataRequired()])
    imagen = FileField('Imagen de Cabecera', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'webp'], 'Solo se permiten imágenes.')])
    submit = SubmitField('Escribir en Bitácora')


class TesoroForm(FlaskForm):
    """Formulario para el Inventario (Bosque/Tienda)."""
    producto = StringField('Nombre del Tesoro', validators=[DataRequired(), Length(max=150)])
    categoria = SelectField('Categoría', choices=[('fisico', '📦 Físico'), ('digital', '💾 Digital')], validators=[DataRequired()])
    precio = DecimalField('Precio (COP)', validators=[DataRequired(), NumberRange(min=0)])
    stock_disponible = IntegerField('Stock Disponible (0 si es digital)', validators=[Optional(), NumberRange(min=0)])
    descripcion = TextAreaField('Descripción del Tesoro', validators=[Optional()])
    imagen = FileField('Imagen del Producto', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'webp'], 'Solo se permiten imágenes.')])
    submit = SubmitField('Añadir al Inventario')
