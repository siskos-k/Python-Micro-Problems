const apiKey = "api"; // Replace with your actual API key
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
