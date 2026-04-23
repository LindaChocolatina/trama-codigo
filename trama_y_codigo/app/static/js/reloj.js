/**
 * Reloj del Jardín — Detección de hora y cambio de estados.
 * El frontend sincroniza con el backend para saber en qué franja estamos.
 */
(function() {
    'use strict';

    function obtenerFranja() {
        const ahora = new Date();
        const h = ahora.getHours();
        const m = ahora.getMinutes();
        const min = h * 60 + m;
        if (min >= 331 && min <= 1100) return 'solar';
        return 'nocturno';
    }

    function aplicarEstado() {
        const franja = obtenerFranja();
        const escena = document.querySelector('.escena-paisaje');
        if (!escena) return;
        escena.classList.remove('modo-solar', 'modo-nocturno');
        escena.classList.add('modo-' + franja);

        const fondoSolar = document.querySelector('.escena-fondo--solar');
        const fondoNocturno = document.querySelector('.escena-fondo--nocturno');
        if (fondoSolar && fondoNocturno) {
            if (franja === 'solar') {
                fondoSolar.style.opacity = '1';
                fondoNocturno.style.opacity = '0';
            } else {
                fondoSolar.style.opacity = '0';
                fondoNocturno.style.opacity = '1';
            }
        }

        const indicador = document.getElementById('indicador-hora');
        if (indicador) {
            const ahora = new Date();
            const horas = String(ahora.getHours()).padStart(2, '0');
            const mins = String(ahora.getMinutes()).padStart(2, '0');
            const emoji = franja === 'solar' ? '☀️' : '🌙';
            indicador.textContent = emoji + ' ' + horas + ':' + mins;
        }
    }

    function aplicarEstadoGlobal() {
        const franja = obtenerFranja();
        document.body.classList.remove('modo-solar', 'modo-nocturno');
        document.body.classList.add('modo-' + franja);
    }

    document.addEventListener('DOMContentLoaded', function() {
        aplicarEstado();
        aplicarEstadoGlobal();
        setInterval(function() {
            aplicarEstado();
            aplicarEstadoGlobal();
        }, 60000);
    });
})();
