document.addEventListener("DOMContentLoaded", function () {
  const modeToggle = document.getElementById("modeToggle");

  modeToggle.addEventListener("click", function () {
    document.body.classList.toggle("dark-mode");

    // Optionally save the current mode to local storage
    if (document.body.classList.contains("dark-mode")) {
      localStorage.setItem("theme", "dark");
    } else {
      localStorage.setItem("theme", "light");
    }
  });

  // Check for saved theme preference, if any
  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
  }
});
