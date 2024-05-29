document.addEventListener("DOMContentLoaded", () => {
  const players = [
    { name: "Pele" },
    { name: "Diego Maradona" },
    { name: "Lionel Messi" },
    { name: "Cristiano Ronaldo" },
    { name: "Johan Cruyff" },
    { name: "Franz Beckenbauer" },
    { name: "Zinedine Zidane" },
    { name: "Ronaldo Nazario" },
    { name: "Gerd Muller" },
    { name: "Alfredo Di Stefano" },
  ];

  let currentPlayer = players[Math.floor(Math.random() * players.length)];
  let remainingPlayers = [...players]; // Make a copy

  const player1El = document.getElementById("player1");
  const player2El = document.getElementById("player2");
  const questionEl = document.getElementById("question");
  const resultEl = document.getElementById("result");
  const goatEl = document.getElementById("goat");

  // Function to display a new question (or end the game)
  function handleNextQuestion() {
    remainingPlayers = remainingPlayers.filter((p) => p !== currentPlayer);

    if (remainingPlayers.length === 0) {
      // Game Over
      questionEl.style.display = "none";
      goatEl.textContent = currentPlayer.name;
      resultEl.style.display = "block";
    } else {
      const opponentIndex = Math.floor(Math.random() * remainingPlayers.length);
      const opponent = remainingPlayers.splice(opponentIndex, 1)[0];
      player1El.textContent = currentPlayer.name;
      player2El.textContent = opponent.name;
    }
  }

  // Handle button clicks
  document.getElementById("yesButton").addEventListener("click", () => {
    handleNextQuestion();
  });

  document.getElementById("noButton").addEventListener("click", () => {
    currentPlayer = remainingPlayers.find(
      (p) => p.name === player2El.textContent,
    );
    handleNextQuestion();
  });

  // Initial question
  handleNextQuestion();
});
