const signupForm = document.getElementById("signup-form");

signupForm.addEventListener("submit", function (e) {
  e.preventDefault(); // Prevent default form submission

  // You would handle form data submission to your mailing list service here
  // Example:
  const email = document.querySelector('input[name="email"]').value;
  console.log("Email for signup:", email);

  // Display a success message or reset the form (optional)
});
