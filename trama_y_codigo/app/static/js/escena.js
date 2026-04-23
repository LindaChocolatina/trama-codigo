/**
 * Escena — Animaciones del paisaje.
 * Luciérnagas, estrellas y efectos atmosféricos.
 */
(function() {
    'use strict';

    function crearLuciernagas(contenedor, cantidad) {
        for (let i = 0; i < cantidad; i++) {
            const luz = document.createElement('div');
            luz.classList.add('luciernaga');
            luz.style.left = Math.random() * 100 + '%';
            luz.style.top = 20 + Math.random() * 60 + '%';
            luz.style.animationDelay = Math.random() * 4 + 's';
            luz.style.animationDuration = (3 + Math.random() * 3) + 's';
            contenedor.appendChild(luz);
        }
    }

    function crearEstrellas(contenedor, cantidad) {
        for (let i = 0; i < cantidad; i++) {
            const estrella = document.createElement('div');
            estrella.classList.add('estrella');
            estrella.style.left = Math.random() * 100 + '%';
            estrella.style.top = Math.random() * 40 + '%';
            estrella.style.animationDelay = Math.random() * 3 + 's';
            estrella.style.animationDuration = (2 + Math.random() * 4) + 's';
            const size = 1 + Math.random() * 2;
            estrella.style.width = size + 'px';
            estrella.style.height = size + 'px';
            contenedor.appendChild(estrella);
        }
    }

    function inicializarEscena() {
        const escena = document.querySelector('.escena-paisaje');
        if (!escena) return;

        const esNoche = escena.classList.contains('modo-nocturno');
        // Limpiar elementos previos
        escena.querySelectorAll('.luciernaga, .estrella').forEach(function(el) { el.remove(); });

        if (esNoche) {
            crearLuciernagas(escena, 15);
            crearEstrellas(escena, 40);
        }
    }

    // Observar cambios de clase en la escena
    document.addEventListener('DOMContentLoaded', function() {
        inicializarEscena();
        const escena = document.querySelector('.escena-paisaje');
        if (escena) {
            const observer = new MutationObserver(function() { inicializarEscena(); });
            observer.observe(escena, { attributes: true, attributeFilter: ['class'] });
        }
    });
})();
