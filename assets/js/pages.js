/* Interior-page behaviour. Progressive: every page reads fine without it. */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* --------------------------------------------------------- sliders --- */
  $$('[data-slider]').forEach(function (root) {
    var rail = $('[data-rail]', root),
        prev = $('[data-prev]', root),
        next = $('[data-next]', root);
    if (!rail || !prev || !next) return;

    function step() {
      var slide = rail.firstElementChild;
      if (!slide) return rail.clientWidth;
      var gap = parseFloat(getComputedStyle(rail).gap) || 0;
      return slide.getBoundingClientRect().width + gap;
    }
    function sync() {
      prev.disabled = rail.scrollLeft < 4;
      next.disabled = rail.scrollLeft > rail.scrollWidth - rail.clientWidth - 4;
    }
    function go(dir) {
      rail.scrollBy({ left: dir * step(), behavior: reduce ? 'auto' : 'smooth' });
    }
    prev.addEventListener('click', function () { go(-1); });
    next.addEventListener('click', function () { go(1); });
    rail.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
    sync();

    // drag with a mouse; touch already works natively
    var down = false, startX = 0, startL = 0, moved = 0;
    rail.addEventListener('pointerdown', function (e) {
      if (e.pointerType === 'touch') return;
      down = true; moved = 0; startX = e.clientX; startL = rail.scrollLeft;
      rail.setPointerCapture(e.pointerId); rail.style.cursor = 'grabbing';
    });
    rail.addEventListener('pointermove', function (e) {
      if (!down) return;
      var d = e.clientX - startX; moved = Math.abs(d); rail.scrollLeft = startL - d;
    });
    ['pointerup', 'pointercancel'].forEach(function (ev) {
      rail.addEventListener(ev, function () { down = false; rail.style.cursor = ''; });
    });
    rail.addEventListener('click', function (e) { if (moved > 6) e.preventDefault(); }, true);
    rail.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { go(1); e.preventDefault(); }
      if (e.key === 'ArrowLeft')  { go(-1); e.preventDefault(); }
    });
  });

  /* ------------------------------------------- bars and timeline dots --- */
  var draws = $$('[data-compare], .tl');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.2 });
    draws.forEach(function (el) { io.observe(el); });
  } else {
    draws.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ------------------------------------------------------ table of c --- */
  $$('[data-toc]').forEach(function (toc) {
    var links = $$('a[href^="#"]', toc);
    if (!links.length) return;
    var targets = links.map(function (a) {
      return document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
    });

    function mark() {
      var best = -1, y = window.scrollY + window.innerHeight * 0.28;
      targets.forEach(function (t, i) {
        if (t && t.getBoundingClientRect().top + window.scrollY <= y) best = i;
      });
      links.forEach(function (a, i) { a.classList.toggle('is-here', i === best); });
    }
    var ticking = false;
    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () { mark(); ticking = false; });
    }, { passive: true });
    mark();
  });
})();
