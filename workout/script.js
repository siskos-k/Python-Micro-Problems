var modal = document.getElementById("genderModal");
var btn = document.getElementById("getStartedBtn");

// When the user clicks the button, open the modal
btn.onclick = function () {
  modal.style.display = "block";
};

// Redirect function
function redirectToPage(page) {
  window.location.href = page;
}
// Redirect to the workout page
//Redirect to the workout page
// Function to redirect to the workout page with body type
function redirectToWorkout(bodyType) {
  window.location.href = "workout.html?bodyType=" + bodyType;
}

// Function to display selected body type on workout page
window.onload = function () {
  const urlParams = new URLSearchParams(window.location.search);
  const bodyType = urlParams.get("bodyType");

  if (bodyType) {
    const bodyTypeText = document.getElementById("selectedBodyType");
    let bodyTypeName;
    switch (bodyType) {
      case "1":
        bodyTypeName = "Slim";
        break;
      case "2":
        bodyTypeName = "Fit";
        break;
      case "3":
        bodyTypeName = "Medium";
        break;
      case "4":
        bodyTypeName = "Large";
        break;
      default:
        bodyTypeName = "Unknown";
    }
    bodyTypeText.textContent += bodyTypeName; // Append the body type name to the existing text
  }
};
