const sections = document.querySelectorAll("section");

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
      if (entry.isIntersecting) {
          entry.target.style.opacity = "1";
          entry.target.style.transform = "translateY(0)";
      } else {
          entry.target.style.opacity = "0";
          entry.target.style.transform = "translateY(20px)";
      }
  });
}, { threshold: 0.5 });

sections.forEach((section) => {
  section.style.opacity = "0";
  section.style.transform = "translateY(20px)";
  section.style.transition = "opacity .6s ease-out, transform .6s ease-out";
  observer.observe(section);
});
