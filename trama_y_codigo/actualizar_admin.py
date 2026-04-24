from app import create_app
from app.extensions import db
from app.models.usuario import Usuario

def actualizar_credenciales():
    app = create_app()
    with app.app_context():
        print("🌿 Actualizador de Credenciales - Trama & Código")
        print("-------------------------------------------------")
        
        jardinera = Usuario.query.filter_by(rol='administradora').first()
        
        if not jardinera:
            print("No se encontró el perfil de administradora en la base de datos.")
            return

        print(f"Perfil actual: {jardinera.email} ({jardinera.username})")
        print("Si no deseas cambiar un dato, simplemente presiona ENTER sin escribir nada.\n")

        nuevo_username = input(f"Nuevo apodo [actual: {jardinera.username}]: ").strip()
        nuevo_email = input(f"Nuevo correo electrónico [actual: {jardinera.email}]: ").strip()
        nueva_contrasena = input("Nueva contraseña (mínimo 6 caracteres) [dejar en blanco para no cambiar]: ").strip()

        cambios = False

        if nuevo_username:
            jardinera.username = nuevo_username
            cambios = True
        
        if nuevo_email:
            jardinera.email = nuevo_email
            cambios = True
            
        if nueva_contrasena:
            jardinera.plantar_contrasena(nueva_contrasena)
            cambios = True

        if cambios:
            db.session.commit()
            print("\n✅ ¡Tus nuevas credenciales han sido sembradas exitosamente!")
            print(f"Tu nuevo correo de ingreso es: {jardinera.email}")
        else:
            print("\nNo se realizaron cambios.")

if __name__ == '__main__':
    actualizar_credenciales()
