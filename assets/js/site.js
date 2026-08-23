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
  // publish the real masthead height so the hero can clear it on phones
  function measureHeader() {
    document.documentElement.style.setProperty('--hdr-h', header.offsetHeight + 'px');
  }
  onScrollHeader();
  measureHeader();
  window.addEventListener('load', measureHeader);

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
  // sections whose bars/rules draw themselves once they come into view
  var drawSecs = [scaleSec, $('.revs')].filter(Boolean);
  if ('IntersectionObserver' in window) {
    var xo = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); xo.unobserve(en.target); }
      });
    }, { threshold: 0.2 });
    drawSecs.forEach(function (el) { xo.observe(el); });
  } else {
    drawSecs.forEach(function (el) { el.classList.add('is-in'); });
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

  /* -------------------------------------------------------- reviews ---- */
  var scroller = $('#revScroll');

  function wireReviews() {
    $$('.rev').forEach(function (rev) {
      var body = $('.rev__body', rev), btn = $('.rev__more', rev);
      if (!body || !btn) return;
      var collapsed = body.offsetHeight;

      // only offer the control when there is actually more to read
      if (body.scrollHeight <= collapsed + 4) { btn.hidden = true; return; }
      btn.hidden = false;

      btn.addEventListener('click', function () {
        var open = rev.getAttribute('data-open') === 'true';
        if (open) {
          body.style.height = body.scrollHeight + 'px';   // fix the start value
          requestAnimationFrame(function () { body.style.height = collapsed + 'px'; });
          rev.setAttribute('data-open', 'false');
          btn.setAttribute('aria-expanded', 'false');
          btn.textContent = 'Read more';
        } else {
          body.style.height = body.scrollHeight + 'px';
          rev.setAttribute('data-open', 'true');
          btn.setAttribute('aria-expanded', 'true');
          btn.textContent = 'Show less';
        }
      });

      // once expanded, let the text reflow freely
      body.addEventListener('transitionend', function (e) {
        if (e.propertyName === 'height' && rev.getAttribute('data-open') === 'true') {
          body.style.height = 'auto';
        }
      });
    });
  }

  // measure only once the webfonts are in, or the line count is wrong
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(wireReviews);
  } else {
    window.addEventListener('load', wireReviews);
  }

  if (scroller) {
    var panel = scroller.parentElement;

    var onRevScroll = function () {
      var atEnd = scroller.scrollTop + scroller.clientHeight >= scroller.scrollHeight - 24;
      panel.classList.toggle('is-end', atEnd);
    };
    scroller.addEventListener('scroll', onRevScroll, { passive: true });
    onRevScroll();

    /* Ambient autoscroll: a slow drift that signals there is more to read.
       It yields to the reader — any hover, focus, or manual scroll stops it,
       and it resumes only after they have been idle for a moment. */
    if (!reduce) {
      var SPEED = 16;        // px per second
      var IDLE = 4000;       // ms of stillness before drifting again
      var running = false, visible = false, held = false;
      var raf = null, last = 0, expected = 0, idleTimer = null, rewinding = false;

      function maxScroll() { return scroller.scrollHeight - scroller.clientHeight; }

      function frame(ts) {
        if (!running) return;
        if (!last) last = ts;
        var dt = Math.min((ts - last) / 1000, 0.05);
        last = ts;

        if (!rewinding) {
          var max = maxScroll();
          if (max <= 0) { raf = requestAnimationFrame(frame); return; }
          expected = Math.min(expected + SPEED * dt, max);
          scroller.scrollTop = expected;
          if (expected >= max - 0.5) rewind();
        }
        raf = requestAnimationFrame(frame);
      }

      function rewind() {
        rewinding = true;
        var from = scroller.scrollTop, t0 = null;
        setTimeout(function () {
          function back(ts) {
            if (!running) { rewinding = false; return; }
            if (t0 === null) t0 = ts;
            var p = Math.min((ts - t0) / 900, 1);
            var eased = p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
            expected = from * (1 - eased);
            scroller.scrollTop = expected;
            if (p < 1) requestAnimationFrame(back);
            else { expected = 0; rewinding = false; }
          }
          requestAnimationFrame(back);
        }, 1400);
      }

      function start() {
        if (running || held || !visible) return;
        running = true; last = 0; expected = scroller.scrollTop;
        raf = requestAnimationFrame(frame);
      }
      function stop() {
        running = false; rewinding = false;
        if (raf) { cancelAnimationFrame(raf); raf = null; }
      }
      function holdThenResume() {
        held = true; stop();
        clearTimeout(idleTimer);
        idleTimer = setTimeout(function () { held = false; start(); }, IDLE);
      }

      // a reader taking over always wins
      scroller.addEventListener('scroll', function () {
        if (running && !rewinding && Math.abs(scroller.scrollTop - expected) > 2) holdThenResume();
      }, { passive: true });
      ['wheel', 'touchstart', 'keydown'].forEach(function (ev) {
        scroller.addEventListener(ev, holdThenResume, { passive: true });
      });
      panel.addEventListener('pointerenter', function () { held = true; stop(); clearTimeout(idleTimer); });
      panel.addEventListener('pointerleave', function () { held = false; clearTimeout(idleTimer); start(); });
      panel.addEventListener('focusin', function () { held = true; stop(); clearTimeout(idleTimer); });
      panel.addEventListener('focusout', function (e) {
        if (!panel.contains(e.relatedTarget)) { held = false; start(); }
      });
      $$('.rev__more').forEach(function (btn) { btn.addEventListener('click', holdThenResume); });

      // only drift while the section is actually on screen
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (entries) {
          entries.forEach(function (en) {
            visible = en.isIntersecting;
            if (visible) start(); else stop();
          });
        }, { threshold: 0.25 }).observe(panel);
      } else {
        visible = true; start();
      }
      document.addEventListener('visibilitychange', function () {
        if (document.hidden) stop(); else start();
      });
    }
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
  window.addEventListener('resize', function () { buildTicks(); measureHeader(); onScrollSpine(); });

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
