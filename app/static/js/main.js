// Carloszerpav: micro-interacciones mínimas
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReducedMotion) {
  document.addEventListener('mousemove', (e) => {
    const header = document.querySelector('.site-header');
    if (!header) return;
    const dx = (e.clientX / window.innerWidth - 0.5) * 2;
    header.style.boxShadow = `${dx * 8}px 8px 24px rgba(0,0,0,0.2)`;
  });
}

// Marcar página activa en el nav
document.addEventListener('DOMContentLoaded', () => {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav a');
  navLinks.forEach(link => {
    const linkPath = new URL(link.href).pathname;
    if (linkPath === currentPath || (currentPath === '/' && linkPath === '/')) {
      link.classList.add('active');
    }
  });
});
