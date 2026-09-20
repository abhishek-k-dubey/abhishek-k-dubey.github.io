(() => {
  'use strict';
  const views = [...document.querySelectorAll('.view')];
  const navigation = document.querySelector('#main-nav');
  const menuButton = document.querySelector('.menu-toggle');
  const main = document.querySelector('#main');
  const viewIds = new Set(views.map(view => view.id));
  const closeMenu = () => {
    navigation.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.textContent = 'Menu';
  };
  function showRoute({ moveFocus = true } = {}) {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { id = 'overview'; }
    if (id === 'main') id = 'overview';
    let target = document.getElementById(id);
    let active = viewIds.has(id) ? target : target?.closest('.view');
    if (!active) {
      active = document.getElementById('overview');
      target = active;
    }
    views.forEach(view => { view.hidden = view !== active; });
    const section = active.dataset.parent || active.id;
    navigation.querySelectorAll('[data-nav]').forEach(link => {
      if (link.dataset.nav === section) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
    document.title = `${active.dataset.title} | Abhishek K. Dubey, Ph.D.`;
    closeMenu();
    if (target !== active) {
      // A shared fragment reveals its containing page and any closed details.
      let ancestor = target;
      while (ancestor && ancestor !== active) {
        if (ancestor.tagName === 'DETAILS') ancestor.open = true;
        ancestor = ancestor.parentElement;
      }
      if (moveFocus) {
        const heading = target.tagName === 'DETAILS'
          ? target.querySelector('summary')
          : target.querySelector('h2, h3') || target;
        heading.setAttribute('tabindex', '-1');
        heading.focus({ preventScroll: true });
      }
      target.scrollIntoView({ block: 'start', behavior: 'instant' });
    } else if (moveFocus) {
      active.querySelector('h1').focus({ preventScroll: true });
      window.scrollTo({ top: 0, behavior: 'instant' });
    }
  }
  document.documentElement.classList.add('js');
  menuButton.hidden = false;
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.textContent = open ? 'Close' : 'Menu';
    navigation.classList.toggle('open', open);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && navigation.classList.contains('open')) {
      closeMenu();
      menuButton.focus();
    }
  });
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#"]');
    if (link && link.hash === '#main') { event.preventDefault(); main.focus(); return; }
    if (link && link.hash === location.hash && link.hash !== '#main') showRoute();
  });
  window.addEventListener('hashchange', () => showRoute());
  document.querySelectorAll('[data-filter]').forEach(button => {
    button.addEventListener('click', () => {
      const filter = button.dataset.filter;
      document.querySelectorAll('[data-filter]').forEach(other => other.setAttribute('aria-pressed', String(other === button)));
      let count = 0;
      document.querySelectorAll('.work-all .work-card').forEach(card => {
        const show = filter === 'all' || card.dataset.category === filter;
        card.hidden = !show;
        if (show) count++;
      });
      document.querySelector('#filter-status').textContent = `${count} ${count === 1 ? 'project' : 'projects'} shown.`;
    });
  });
  document.querySelector('#year').textContent = new Date().getFullYear();
  showRoute({ moveFocus: false });
})();
