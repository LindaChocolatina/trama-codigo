/**
 * Hechizos — Easter Eggs del jardín.
 * "La normalidad nunca ha creado magia"
 */
(function() {
    'use strict';

    var frases = [
        "Normal never created magic",
        "Create the things you wish existed",
        "There is a healing power in the act of creating",
        "Diseño y programo como si mi alma fuera requerida",
        "La normalidad nunca ha creado magia",
        "El código es poesía que la máquina puede leer"
    ];

    function lanzarHechizo(mensaje) {
        // Crear pergamino
        var pergamino = document.createElement('div');
        pergamino.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);' +
            'background:rgba(245,240,232,0.95);backdrop-filter:blur(20px);padding:40px 50px;' +
            'border-radius:16px;border:1px solid rgba(192,149,40,0.3);z-index:9999;text-align:center;' +
            'box-shadow:0 20px 60px rgba(0,0,0,0.2);animation:aparecer 0.6s ease;max-width:500px;';
        pergamino.innerHTML = '<p style="font-family:Caveat,cursive;font-size:1.6rem;color:#630E16;margin:0;line-height:1.5;">' +
            '"' + mensaje + '"</p>';

        // Crear partículas
        crearParticulas();

        document.body.appendChild(pergamino);
        setTimeout(function() {
            pergamino.style.transition = 'opacity 1s ease';
            pergamino.style.opacity = '0';
            setTimeout(function() { pergamino.remove(); }, 1000);
        }, 4000);
    }

    function crearParticulas() {
        for (var i = 0; i < 20; i++) {
            var particula = document.createElement('div');
            var x = Math.random() * window.innerWidth;
            var y = Math.random() * window.innerHeight;
            particula.style.cssText = 'position:fixed;left:' + x + 'px;top:' + y + 'px;' +
                'width:6px;height:6px;background:' + (Math.random() > 0.5 ? '#C09528' : '#D97D3A') + ';' +
                'border-radius:50%;z-index:10000;pointer-events:none;' +
                'box-shadow:0 0 10px currentColor;' +
                'animation:particula-flotar ' + (1 + Math.random() * 2) + 's ease forwards;';
            document.body.appendChild(particula);
            setTimeout(function() { particula.remove(); }, 3000);
        }
    }

    // CSS para animación de partículas
    var style = document.createElement('style');
    style.textContent = '@keyframes particula-flotar{0%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(0) translateY(-100px)}}';
    document.head.appendChild(style);

    // Easter Egg 1: Escribir "CREAR"
    var secuencia = '';
    document.addEventListener('keypress', function(e) {
        secuencia += e.key.toUpperCase();
        if (secuencia.length > 5) secuencia = secuencia.slice(-5);
        if (secuencia === 'CREAR') {
            lanzarHechizo(frases[Math.floor(Math.random() * frases.length)]);
            secuencia = '';
        }
    });

    // Easter Egg 2: Luciérnaga clickeable (noche)
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('luciernaga')) {
            lanzarHechizo("Normal never created magic");
        }
    });

    // Exponer función globalmente para otros usos
    window.lanzarHechizo = lanzarHechizo;
})();
