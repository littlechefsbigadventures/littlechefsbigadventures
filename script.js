// 🔹 Highlight current nav link on scroll
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('.section, .hero');
  const navLinks = document.querySelectorAll('nav a');

  let currentSection = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop - 150;
    if (pageYOffset >= sectionTop) {
      currentSection = section.getAttribute('id');
    }
  });

  navLinks.forEach(link => {
    link.classList.remove('active');
    if (currentSection && link.getAttribute('href').includes(currentSection)) {
      link.classList.add('active');
    }
  });
});

// 🔹 Newsletter form frontend feedback (no backend yet)
document.querySelector('form')?.addEventListener('submit', (e) => {
  e.preventDefault();
  alert('🎉 Thank you for signing up! Stay tuned for delicious updates!');
  e.target.reset();
});
