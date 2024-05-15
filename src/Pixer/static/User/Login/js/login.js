document.addEventListener("DOMContentLoaded", (event) => {
  const form = document.getElementById("login-form");
  form.addEventListener("submit", (event) => {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Perform validation or AJAX request here
    console.log("Username:", username);
    console.log("Password:", password);

    // Example: alert on successful submission
    alert("Login form submitted!");

    // If using AJAX, handle the response and update the UI accordingly
  });
});
