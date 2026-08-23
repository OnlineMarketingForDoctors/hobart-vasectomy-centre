/* Hobart Vasectomy Centre — interaction layer.
   Everything here is progressive: the page is fully readable without it. */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------------------------------------------------------- header --- */
  var header = $('#siteHeader');
  function onScrollHeader() {
    header.classList.toggle('is-stuck', window.scrollY > 40);
  }
  onScrollHeader();

  /* ---------------------------------------------------------- drawer --- */
  var burger = $('#burger'), drawer = $('#drawer');
  function setDrawer(open) {
    drawer.setAttribute('data-open', open ? 'true' : 'false');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    document.body.style.overflow = open ? 'hidden' : '';
  }
  burger.addEventListener('click', function () {
    setDrawer(drawer.getAttribute('data-open') !== 'true');
  });
  $$('a', drawer).forEach(function (a) {
    a.addEventListener('click', function () { setDrawer(false); });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && drawer.getAttribute('data-open') === 'true') {
      setDrawer(false); burger.focus();
    }
  });

  /* ---------------------------------------------------------- reveals --- */
  var revs = $$('[data-rev]');
  if ('IntersectionObserver' in window && !reduce) {
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); ro.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
    revs.forEach(function (el) { ro.observe(el); });
  } else {
    revs.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* steps get their own marker state */
  var steps = $$('.step');
  if ('IntersectionObserver' in window) {
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) en.target.classList.add('is-in'); });
    }, { rootMargin: '0px 0px -30% 0px', threshold: 0.2 });
    steps.forEach(function (el) { so.observe(el); });
  }

  /* ----------------------------------------------------- count-ups ----- */
  function fmt(n) { return n.toLocaleString('en-AU'); }
  function countUp(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    if (isNaN(target)) return;
    if (reduce) { el.textContent = fmt(target) + suffix; return; }
    var dur = 1500, t0 = null;
    function tick(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(Math.round(target * eased)) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  var counters = $$('[data-count]');
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { countUp(en.target); co.unobserve(en.target); }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { co.observe(el); });
  }

  /* ------------------------------------------------------- spine ------- */
  var spineTicks = $('#spineTicks'),
      spineProg  = $('#spineProgress'),
      spineLabel = $('#spineLabel'),
      spineCount = $('#spineCount');

  function buildTicks() {
    if (!spineTicks) return;
    spineTicks.innerHTML = '';
    var h = window.innerHeight, step = 13, n = Math.ceil(h / step), frag = document.createDocumentFragment();
    for (var i = 0; i <= n; i++) {
      var b = document.createElement('i');
      b.className = 'spine__tick' + (i % 5 === 0 ? ' spine__tick--major' : '');
      b.style.top = (i * step) + 'px';
      frag.appendChild(b);
    }
    spineTicks.appendChild(frag);
  }

  var sections = $$('[data-spine]');
  var currentLabel = '';
  function onScrollSpine() {
    var doc = document.documentElement;
    var max = doc.scrollHeight - window.innerHeight;
    var pct = max > 0 ? Math.min(Math.max(window.scrollY / max, 0), 1) : 0;
    if (spineProg) spineProg.style.height = (pct * 100) + '%';
    if (spineCount) spineCount.textContent = String(Math.round(pct * 100)).padStart(2, '0') + '%';

    var mid = window.scrollY + window.innerHeight * 0.36, found = '';
    for (var i = 0; i < sections.length; i++) {
      var r = sections[i].getBoundingClientRect();
      var top = r.top + window.scrollY;
      if (mid >= top) found = sections[i].getAttribute('data-spine');
    }
    if (found && found !== currentLabel && spineLabel) {
      currentLabel = found;
      spineLabel.style.opacity = '0';
      setTimeout(function () { spineLabel.textContent = currentLabel; spineLabel.style.opacity = '1'; }, 180);
    }
  }

  /* ------------------------------------------------------ pillars ------ */
  var pillars = $$('.pillar'), pillarImgs = $$('.pillars__media img');
  function setPillar(i) {
    pillars.forEach(function (p) { p.classList.toggle('is-active', +p.getAttribute('data-i') === i); });
    pillarImgs.forEach(function (im) { im.classList.toggle('is-active', +im.getAttribute('data-i') === i); });
  }
  pillars.forEach(function (p) {
    p.addEventListener('mouseenter', function () { setPillar(+p.getAttribute('data-i')); });
  });
  if ('IntersectionObserver' in window && pillars.length) {
    var po = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) setPillar(+en.target.getAttribute('data-i'));
      });
    }, { rootMargin: '-42% 0px -42% 0px', threshold: 0 });
    pillars.forEach(function (p) { po.observe(p); });
  }

  /* --------------------------------------------------------- scale ----- */
  var scaleTicks = $('#scaleTicks'), scaleSec = $('.scale');
  if (scaleTicks) {
    var f = document.createDocumentFragment();
    for (var k = 0; k <= 48; k++) {
      var t = document.createElement('b');
      t.style.left = (k / 48 * 100) + '%';
      if (k % 12 === 0) t.style.height = '13px';
      f.appendChild(t);
    }
    scaleTicks.appendChild(f);
  }
  if (scaleSec && 'IntersectionObserver' in window) {
    var xo = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { scaleSec.classList.add('is-in'); xo.unobserve(en.target); }
      });
    }, { threshold: 0.25 });
    xo.observe(scaleSec);
  }

  /* ----------------------------------------------------------- faq ----- */
  $$('.qa').forEach(function (qa) {
    var btn = $('.qa__q', qa), panel = $('.qa__a', qa), inner = $('.qa__a-in', qa);
    function open(state) {
      qa.setAttribute('data-open', state ? 'true' : 'false');
      btn.setAttribute('aria-expanded', state ? 'true' : 'false');
      panel.style.height = state ? inner.offsetHeight + 'px' : '0px';
    }
    if (qa.getAttribute('data-open') === 'true') panel.style.height = inner.offsetHeight + 'px';
    btn.addEventListener('click', function () {
      var willOpen = qa.getAttribute('data-open') !== 'true';
      $$('.qa').forEach(function (other) {
        if (other !== qa && other.getAttribute('data-open') === 'true') {
          other.setAttribute('data-open', 'false');
          $('.qa__q', other).setAttribute('aria-expanded', 'false');
          $('.qa__a', other).style.height = '0px';
        }
      });
      open(willOpen);
    });
    window.addEventListener('resize', function () {
      if (qa.getAttribute('data-open') === 'true') panel.style.height = inner.offsetHeight + 'px';
    });
  });

  /* ---------------------------------------------------------- rail ----- */
  var rail = $('#rail');
  if (rail) {
    var down = false, startX = 0, startL = 0, moved = 0;
    rail.addEventListener('pointerdown', function (e) {
      if (e.pointerType === 'touch') return;
      down = true; moved = 0;
      startX = e.clientX; startL = rail.scrollLeft;
      rail.classList.add('is-drag');
      rail.setPointerCapture(e.pointerId);
    });
    rail.addEventListener('pointermove', function (e) {
      if (!down) return;
      var d = e.clientX - startX;
      moved = Math.abs(d);
      rail.scrollLeft = startL - d;
    });
    ['pointerup', 'pointercancel'].forEach(function (ev) {
      rail.addEventListener(ev, function () { down = false; rail.classList.remove('is-drag'); });
    });
    rail.addEventListener('click', function (e) { if (moved > 6) e.preventDefault(); }, true);
    rail.addEventListener('keydown', function (e) {
      var card = $('.rev', rail);
      var w = card ? card.offsetWidth + 24 : 400;
      if (e.key === 'ArrowRight') { rail.scrollBy({ left: w, behavior: reduce ? 'auto' : 'smooth' }); e.preventDefault(); }
      if (e.key === 'ArrowLeft')  { rail.scrollBy({ left: -w, behavior: reduce ? 'auto' : 'smooth' }); e.preventDefault(); }
    });
  }

  /* ------------------------------------------------------- listeners --- */
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      onScrollHeader(); onScrollSpine(); ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', function () { buildTicks(); onScrollSpine(); });

  buildTicks();
  onScrollSpine();

  /* smooth in-page anchors, respecting reduced motion */
  $$('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href');
      if (id.length < 2) return;
      var t = document.querySelector(id);
      if (!t) return;
      e.preventDefault();
      var y = t.getBoundingClientRect().top + window.scrollY - 78;
      window.scrollTo({ top: y, behavior: reduce ? 'auto' : 'smooth' });
    });
  });
})();
