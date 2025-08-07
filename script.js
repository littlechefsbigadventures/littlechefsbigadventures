// Sticky Navigation Highlight
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('.section, .hero');
  const navLinks = document.querySelectorAll('.nav-links a');

  let currentSection = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop - 100;
    if (pageYOffset >= sectionTop) {
      currentSection = section.getAttribute('id');
    }
  });

  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href').includes(currentSection)) {
      link.classList.add('active');
    }
  });
});

// Newsletter popup
document.querySelector('.newsletter-form')?.addEventListener('submit', (e) => {
  e.preventDefault();
  alert('Thank you for signing up! Stay tuned for delicious updates!');
  e.target.reset();
});
