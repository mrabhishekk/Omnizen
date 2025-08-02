 const now = new Date();
  const hour = now.getHours();
  let timeGreeting = "Hello";

  if (hour >= 5 && hour < 12) {
    timeGreeting = "Good morning";
  } else if (hour >= 12 && hour < 17) {
    timeGreeting = "Good afternoon";
  } else {
    timeGreeting = "Good evening";
  }
  
  window.username = "{{ request.user.username|title }}";
  const greetings = [
    `${timeGreeting}, ${username}.`,
    "I'm excited to see you...",
    "Let's finish some tasks...",
  ];

  const searchInput = document.getElementById("search");
  let index = 0;

  function rotatePlaceholder() {
    if (searchInput) {
      searchInput.placeholder = greetings[index];
      index = (index + 1) % greetings.length;
    }
  }

  rotatePlaceholder(); // set initial
  setInterval(rotatePlaceholder, 5000); // rotate every 5 sec