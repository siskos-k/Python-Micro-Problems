const apiKey = "YourApiKey"; // Replace with your actual API key
const trendingUrl =
  "https://api.themoviedb.org/3/trending/movie/day?api_key=" + apiKey;
const forYouUrl =
  "https://api.themoviedb.org/3/movie/top_rated?api_key=" + apiKey;

fetch(forYouUrl)
  .then((response) => response.json())
  .then((data) => {
    displayForYouMovies(data.results);
  })
  .catch((error) => console.error("Error:", error));

// Function to Display For You Movies
function displayForYouMovies(movies) {
  const forYouMoviesContainer = document.getElementById("recommended-movies");

  movies.forEach((movie) => {
    const movieDiv = document.createElement("div");
    movieDiv.classList.add("movie"); // Add a class for styling

    // Add movie information to the div (e.g., title, poster, etc.)
    // Here's a basic example:
    const movieTitle = document.createElement("h3");
    movieTitle.textContent = movie.title;
    movieDiv.appendChild(movieTitle);

    // You'll need to fetch the poster path and construct the image URL
    const posterPath = movie.poster_path;
    if (posterPath) {
      const posterUrl = "https://image.tmdb.org/t/p/w500" + posterPath;
      const posterImg = document.createElement("img");
      posterImg.src = posterUrl;
      movieDiv.appendChild(posterImg);
    }

    forYouMoviesContainer.appendChild(movieDiv);
  });
}

fetch(trendingUrl)
  .then((response) => response.json())
  .then((data) => {
    console.log(data.results);
    displayTrendingMovies(data.results);
  })
  .catch((error) => console.error("Error:", error));

function displayTrendingMovies(movies) {
  const trendingMoviesContainer = document.getElementById("trending-movies");

  movies.forEach((movie) => {
    const movieDiv = document.createElement("div");
    movieDiv.classList.add("movie"); // Add a class for styling

    // Add movie information to the div (e.g., title, poster, etc.)
    // Here's a basic example:
    const movieTitle = document.createElement("h3");
    movieTitle.textContent = movie.title;
    movieDiv.appendChild(movieTitle);

    // You'll need to fetch the poster path and construct the image URL
    const posterPath = movie.poster_path;
    if (posterPath) {
      const posterUrl = "https://image.tmdb.org/t/p/w500" + posterPath;
      const posterImg = document.createElement("img");
      posterImg.src = posterUrl;
      movieDiv.appendChild(posterImg);
    }

    trendingMoviesContainer.appendChild(movieDiv);
  });
}

const searchBar = document.getElementById("search-bar");
const searchResultsContainer = document.createElement("div"); // Create a container for search results

// Ensure searchResultsContainer is appended to the correct section
const searchResultsSection = document.getElementById("search-results");
searchResultsSection.appendChild(searchResultsContainer);

searchResultsContainer.id = "search-results"; // Add an id for styling

searchBar.addEventListener("input", () => {
  const searchTerm = searchBar.value.trim();

  if (searchTerm) {
    const searchUrl = `https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&query=${searchTerm}`;

    fetch(searchUrl)
      .then((response) => response.json())
      .then((data) => {
        displaySearchResults(data.results);
      })
      .catch((error) => console.error("Error:", error));
  } else {
    // Clear search results if the search bar is empty
    searchResultsContainer.innerHTML = "";
  }
});

function displaySearchResults(movies) {
  searchResultsContainer.innerHTML = ""; // Clear previous results

  if (movies.length === 0) {
    searchResultsContainer.innerHTML = "<p>No results found.</p>";
    return;
  }

  movies.forEach((movie) => {
    // Create and append movie elements (similar to displayTrendingMovies)
    const movieDiv = document.createElement("div");
    movieDiv.classList.add("movie");

    const movieTitle = document.createElement("h3");
    movieTitle.textContent = movie.title;
    movieDiv.appendChild(movieTitle);

    const posterPath = movie.poster_path;
    if (posterPath) {
      const posterUrl = "https://image.tmdb.org/t/p/w500" + posterPath;
      const posterImg = document.createElement("img");
      posterImg.src = posterUrl;
      movieDiv.appendChild(posterImg);
    }

    searchResultsContainer.appendChild(movieDiv);
  });
}
