from app import create_app
from app.extensions import db
from app.models.usuario import Usuario

app = create_app('desarrollo')
with app.app_context():
    u = Usuario.query.filter_by(rol='administradora').first()
    if u:
        u.username = 'LindaChocolatina'
        u.email = 'lindasioc@gmail.com'
        u.plantar_contrasena('Juanita1509:)')
        db.session.commit()
        print(f"Credenciales restauradas para {u.username} ({u.email})")
    else:
        print("No se encontró usuario con rol 'administradora'")
