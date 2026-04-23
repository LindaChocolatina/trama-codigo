"""
El Reloj Lógico — El pulso del tiempo en el jardín.

Este servicio determina el estado del mundo basado en la hora local.
El jardín respira y cambia en sincronía con el tiempo del usuario.

MVP: Dos estados principales (Solar / Nocturno)
Futuro: 7 franjas horarias completas.
"""
from datetime import datetime


# ═══════════════════════════════════════════════
# Definición de Franjas Horarias
# ═══════════════════════════════════════════════

FRANJAS_MVP = {
    'solar': {
        'inicio': (5, 31),   # 05:31
        'fin': (18, 20),     # 18:20
        'atmosfera': 'modo-solar',
        'descripcion': 'El jardín despierta bajo la luz difusa del sol.',
        'personajes_visibles': True,
        'ventanas_iluminadas': False,
        'humo_chimenea': True,
        'ropa_tendida': True,
        'luciernagas': False,
        'estrellas': False,
    },
    'nocturno': {
        'inicio': (18, 21),  # 18:21
        'fin': (5, 30),      # 05:30
        'atmosfera': 'modo-nocturno',
        'descripcion': 'La noche abraza el paisaje con luna y luciérnagas.',
        'personajes_visibles': False,
        'ventanas_iluminadas': True,
        'humo_chimenea': False,
        'ropa_tendida': False,
        'luciernagas': True,
        'estrellas': True,
    }
}

# Franjas completas para implementación futura (7 estados)
FRANJAS_COMPLETAS = {
    'madrugada': {
        'rango': ((5, 1), (5, 30)),
        'atmosfera': 'modo-madrugada',
        'descripcion': 'Transición de oscuro a claro, niebla densa.',
        'filtro_css': 'brightness(0.4) saturate(0.6) hue-rotate(10deg)',
    },
    'amanecer': {
        'rango': ((5, 31), (7, 0)),
        'atmosfera': 'modo-amanecer',
        'descripcion': 'Luz fría, niebla persistente. Ella alimenta gallinas, él pastorea.',
        'filtro_css': 'brightness(0.7) saturate(0.8)',
    },
    'manana': {
        'rango': ((7, 1), (11, 0)),
        'atmosfera': 'modo-manana',
        'descripcion': 'Luminoso-brumoso. Ropa tendida, ella corre con los perros.',
        'filtro_css': 'brightness(0.9) saturate(0.9)',
    },
    'mediodia': {
        'rango': ((11, 1), (15, 0)),
        'atmosfera': 'modo-mediodia',
        'descripcion': 'Soleado total. Descanso bajo la sombra.',
        'filtro_css': 'brightness(1.1) saturate(1.1)',
    },
    'tarde': {
        'rango': ((15, 1), (17, 30)),
        'atmosfera': 'modo-tarde',
        'descripcion': 'Calma. Él toca guitarra, ella hace crochet.',
        'filtro_css': 'brightness(0.9) saturate(0.9)',
    },
    'hora_dorada': {
        'rango': ((17, 31), (18, 20)),
        'atmosfera': 'modo-hora-dorada',
        'descripcion': 'Rosas, dorados, violetas. Animales al establo.',
        'filtro_css': 'brightness(0.85) saturate(1.3) sepia(0.2)',
    },
    'noche': {
        'rango': ((18, 21), (5, 0)),
        'atmosfera': 'modo-noche',
        'descripcion': 'Luna, estrellas y luciérnagas. Sin personajes.',
        'filtro_css': 'brightness(0.3) saturate(0.7) hue-rotate(20deg)',
    },
}


def _minutos_del_dia(hora, minuto):
    """Convierte hora:minuto a minutos desde medianoche."""
    return hora * 60 + minuto


def obtener_franja_actual(ahora=None):
    """
    Determina la franja horaria actual del jardín.

    Args:
        ahora: datetime opcional (para testing). Si no se provee, usa la hora actual.

    Returns:
        str: nombre de la franja ('solar' o 'nocturno' en MVP)
    """
    if ahora is None:
        ahora = datetime.now()

    minutos = _minutos_del_dia(ahora.hour, ahora.minute)
    inicio_solar = _minutos_del_dia(5, 31)
    fin_solar = _minutos_del_dia(18, 20)

    if inicio_solar <= minutos <= fin_solar:
        return 'solar'
    return 'nocturno'


def obtener_estado_mundo(ahora=None):
    """
    Obtiene el estado completo del mundo para el frontend.

    Returns:
        dict: Estado del mundo con todas las variables visuales necesarias.
    """
    franja = obtener_franja_actual(ahora)
    estado = FRANJAS_MVP[franja].copy()
    estado['franja'] = franja

    if ahora is None:
        ahora = datetime.now()
    estado['hora_actual'] = ahora.strftime('%H:%M')

    # Ventana iluminada: solo entre 18:30 y 21:00
    minutos = _minutos_del_dia(ahora.hour, ahora.minute)
    ventana_inicio = _minutos_del_dia(18, 30)
    ventana_fin = _minutos_del_dia(21, 0)
    estado['ventana_encendida'] = ventana_inicio <= minutos <= ventana_fin

    return estado


def obtener_saludo(ahora=None):
    """
    Genera un saludo narrativo según la hora.

    Returns:
        str: Saludo poético para el visitante.
    """
    franja = obtener_franja_actual(ahora)

    saludos = {
        'solar': [
            'El jardín te da la bienvenida bajo la luz del día...',
            'Las flores susurran mientras caminas por el sendero...',
            'El sol, escondido tras las nubes, ilumina tu llegada...',
        ],
        'nocturno': [
            'Las luciérnagas iluminan tu camino por el jardín dormido...',
            'La luna y las estrellas te reciben en el silencio...',
            'El jardín descansa, pero su magia sigue viva...',
        ],
    }

    from random import choice
    return choice(saludos.get(franja, saludos['solar']))
