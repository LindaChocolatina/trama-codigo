/**
 * Navegación — Menú responsive y scroll effects.
 */
(function() {
    'use strict';

    document.addEventListener('DOMContentLoaded', function() {
        var nav = document.querySelector('.navegacion');
        var toggle = document.querySelector('.menu-toggle');
        var links = document.querySelector('.navegacion-links');

        // Scroll effect
        if (nav) {
            window.addEventListener('scroll', function() {
                if (window.scrollY > 50) {
                    nav.classList.add('scrolled');
                } else {
                    nav.classList.remove('scrolled');
                }
            });
        }

        // Mobile toggle
        if (toggle && links) {
            toggle.addEventListener('click', function() {
                links.classList.toggle('activo');
            });
        }
    });
})();
