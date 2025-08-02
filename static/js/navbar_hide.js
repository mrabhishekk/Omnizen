

const navbar = document.querySelector('.navbar');

window.addEventListener("scroll", () => {
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop <= 0) {
    navbar.classList.remove("hide"); // Show navbar at the very top
  } else {
    navbar.classList.add("hide"); // Hide as soon as you scroll
  }
});

