const searchBtn = document.getElementById("searchBtn");
const searchInput = document.getElementById("searchInput");
const results = document.getElementById("results");

// Replace these with your own App ID and App Key
const app_id = "ur_api";
const app_key = "ur_app";

searchBtn.addEventListener("click", () => {
  const searchTerm = searchInput.value;
  fetchRecipes(searchTerm);
});

async function fetchRecipes(searchTerm) {
  const url = `https://api.edamam.com/search?q=${searchTerm}&app_id=${app_id}&app_key=${app_key}`;

  try {
    const response = await fetch(url);
    const data = await response.json();
    displayResults(data.hits);
  } catch (error) {
    console.error("Error fetching recipes:", error);
    results.innerHTML = "Oops! An error occurred while fetching recipes.";
  }
}

function displayResults(recipes) {
  results.innerHTML = ""; // Clear previous results

  recipes.forEach((recipe) => {
    const button = document.createElement("button");
    button.textContent = recipe.recipe.label;
    button.classList.add("recipe-button"); // Add a class for styling
    button.addEventListener("click", () => {
      window.open(recipe.recipe.url, "_blank"); // Open recipe in a new tab
    });
    results.appendChild(button);
  });
}
gsap.from("#searchInput", { x: -100, opacity: 0, duration: 1, delay: 0.5 });
