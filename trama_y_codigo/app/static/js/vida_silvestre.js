/**
 * Vida Silvestre — Mariposas y Abejas revoloteando.
 * "Donde hay flores, hay esperanza... y polinizadores."
 */
(function() {
    'use strict';

    document.addEventListener('DOMContentLoaded', function() {
        const contenedor = document.getElementById('escena-principal');
        if (!contenedor) return;

        const esNocturno = contenedor.classList.contains('modo-nocturno');
        const cantidad = 5; // Cantidad de seres voladores

        for (let i = 0; i < cantidad; i++) {
            crearSerVolador(contenedor, esNocturno);
        }
    });

    function crearSerVolador(contenedor, esNocturno) {
        const ser = document.createElement('div');
        ser.className = esNocturno ? 'ser-volador mariposa-nocturna' : 'ser-volador abeja';
        
        // Contenido visual (Emoji o pequeño SVG/forma)
        ser.innerHTML = esNocturno ? '🦋' : '🐝';
        
        contenedor.appendChild(ser);

        // Posición inicial aleatoria
        let x = Math.random() * window.innerWidth;
        let y = Math.random() * window.innerHeight;
        
        function animar() {
            // Movimiento errático "orgánico"
            const destinoX = x + (Math.random() - 0.5) * 300;
            const destinoY = y + (Math.random() - 0.5) * 300;
            
            // Mantener dentro de los límites
            const limitX = Math.max(0, Math.min(window.innerWidth - 30, destinoX));
            const limitY = Math.max(0, Math.min(window.innerHeight - 30, destinoY));

            const duracion = 3000 + Math.random() * 4000;

            const anim = ser.animate([
                { transform: `translate(${x}px, ${y}px) scaleX(${destinoX > x ? 1 : -1})` },
                { transform: `translate(${limitX}px, ${limitY}px) scaleX(${destinoX > x ? 1 : -1})` }
            ], {
                duration: duracion,
                easing: 'ease-in-out',
                fill: 'forwards'
            });

            anim.onfinish = () => {
                x = limitX;
                y = limitY;
                setTimeout(animar, Math.random() * 1000);
            };
        }

        animar();
    }
})();
