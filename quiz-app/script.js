const questionElement = document.getElementById("question");
const answerButtonsElement = document.getElementById("answer-buttons");
const resultElement = document.getElementById("result");

let currentQuestionIndex = 0;
const questions = [
  {
    question: "What is the capital of Germany?",
    answers: [
      { text: "Berlin", correct: true },
      { text: "Paris", correct: false },
      { text: "Rome", correct: false },
      { text: "Madrid", correct: false },
    ],
  },
  {
    question: "What is the capital of Italy?",
    answers: [
      { text: "Venice", correct: false },
      { text: "Rome", correct: true },
      { text: "London", correct: false },
      { text: "Berlin", correct: false },
    ],
  },
  {
    question: "What is the capital of Canada?",
    answers: [
      { text: "Ottawa", correct: true },
      { text: "Toronto", correct: false },
      { text: "Montreal", correct: false },
      { text: "Quebec City", correct: false },
    ],
  },
  {
    question: "What is the capital of Spain?",
    answers: [
      { text: "Barcelona", correct: false },
      { text: "Seville", correct: false },
      { text: "Madrid", correct: true },
      { text: "Valencia", correct: false },
    ],
  },
  {
    question: "What is the capital of Japan?",
    answers: [
      { text: "Beijing", correct: false },
      { text: "Tokyo", correct: true },
      { text: "Kyoto", correct: false },
      { text: "Osaka", correct: false },
    ],
  },
];
function startQuiz() {
  showQuestion();
}

function showQuestion() {
  resetState();
  const currentQuestion = questions[currentQuestionIndex];
  questionElement.innerText = currentQuestion.question;
  currentQuestion.answers.forEach((answer) => {
    const button = document.createElement("button");
    button.innerText = answer.text;
    button.classList.add("btn");
    if (answer.correct) {
      button.dataset.correct = answer.correct;
    }
    button.addEventListener("click", selectAnswer);
    answerButtonsElement.appendChild(button);
  });
}

function resetState() {
  resultElement.innerText = "";
  while (answerButtonsElement.firstChild) {
    answerButtonsElement.removeChild(answerButtonsElement.firstChild);
  }
}

let score = 0;
let mistakes = []; // Array to store mistakes

function selectAnswer(e) {
  const selectedButton = e.target;
  const correct = selectedButton.dataset.correct;
  const currentQuestion = questions[currentQuestionIndex];

  if (correct) {
    score++;
  }
  if (!correct) {
    mistakes.push({
      question: currentQuestion.question,
      yourAnswer: selectedButton.innerText,
      correctAnswer: currentQuestion.answers.find((a) => a.correct).text,
    });
  }

  currentQuestionIndex++;

  if (currentQuestionIndex < questions.length) {
    showQuestion();
  } else {
    displayResults();
  }
}

function displayResults() {
  resultElement.innerHTML = `You scored ${score} out of ${questions.length}`;

  if (mistakes.length > 0) {
    resultElement.innerHTML += `<h3>Mistakes:</h3>`;
    mistakes.forEach((mistake, index) => {
      resultElement.innerHTML += `<p>${index + 1}) Question: ${mistake.question}<br>
            You replied: "${mistake.yourAnswer}", but the correct answer was "${mistake.correctAnswer}"</p>`;
    });
  }
}

startQuiz();
