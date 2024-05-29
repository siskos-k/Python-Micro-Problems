const apiKey = ""; // Replace with your actual API key
const newsContainer = document.getElementById("news-container");

async function fetchNews() {
  try {
    const response = await fetch(
      `https://newsapi.org/v2/top-headlines?country=us&apiKey=${apiKey}`,
      { headers: { "Content-Type": "application/json" } },
    );
    const data = await response.json();

    // Check for successful response
    if (response.status === 200) {
      displayHeadlines(data.articles);
    } else {
      throw new Error("Error fetching news headlines");
    }
  } catch (error) {
    console.error("Error:", error.message);
    // Handle error display to the user
  }
}

function displayHeadlines(headlines) {
  newsContainer.innerHTML = "";
  headlines.forEach((headline) => {
    const newsItem = `
            <div class="news-item">
                <h2>${headline.title}</h2>
                <p>${headline.description}</p>
                <a href="${headline.url}" target="_blank">Read more</a>
            </div>
        `;
    newsContainer.innerHTML += newsItem;
  });
}

// Call the function to fetch and display news
fetchNews();
