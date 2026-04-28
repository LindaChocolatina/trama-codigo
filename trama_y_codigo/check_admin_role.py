from app import create_app
from app.models.usuario import Usuario

app = create_app('desarrollo')
with app.app_context():
    u = Usuario.query.filter_by(username='jardinera').first()
    if u:
        print(f"User: {u.username}, Email: {u.email}, Role: {u.rol}, Hash: {u.password_hash[:10]}")
    else:
        print("No user 'jardinera' found")
