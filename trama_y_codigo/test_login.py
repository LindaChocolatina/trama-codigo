from app import create_app
from app.models.usuario import Usuario
from app.extensions import db

app = create_app('desarrollo')
with app.app_context():
    print("Checking admin user...")
    u = Usuario.query.filter_by(rol='administradora').first()
    if u:
        print(f"Admin found: {u.username} ({u.email})")
        print(f"Checking password 'Juanita1509:)'...")
        if u.verificar_contrasena('Juanita1509:)'):
            print("Password OK!")
        else:
            print("Password WRONG!")
    else:
        print("Admin NOT FOUND!")

    print("\nChecking all users:")
    for user in Usuario.query.all():
        print(f"- {user.username} ({user.email}) [{user.rol}]")
