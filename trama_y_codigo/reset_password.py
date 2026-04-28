from app import create_app
from app.extensions import db
from app.models.usuario import Usuario

app = create_app('desarrollo')
with app.app_context():
    u = Usuario.query.filter_by(username='jardinera').first()
    if u:
        u.plantar_contrasena('semilla2026')
        db.session.commit()
        print(f"Password reset successfully for {u.username}")
    else:
        print("User 'jardinera' not found")
