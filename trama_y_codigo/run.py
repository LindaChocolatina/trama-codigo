"""
Trama & Código — Punto de entrada.
Aquí comienza todo: la semilla germina.

"La normalidad nunca ha creado magia"
"""
from app import create_app

import os
app = create_app(os.environ.get('FLASK_ENV', 'desarrollo'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
