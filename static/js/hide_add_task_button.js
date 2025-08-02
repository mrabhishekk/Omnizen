  const floatingBtn = document.querySelector('.floating-button');
  const footer = document.querySelector('footer');

  const observer = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting) {
        floatingBtn.style.display = 'none';
      } else {
        floatingBtn.style.display = 'block';
      }
    },
    {
      root: null,
      threshold: 0.1,
    }
  );

  observer.observe(footer);