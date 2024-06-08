document.addEventListener("DOMContentLoaded", () => {
  // Find the login button by its class name
  var loginButton = document.getElementById("btnLogin-popup");

  // Add event listener to the login button
  if (loginButton) {
    loginButton.addEventListener("click", function () {
      // Redirect to the login page
      window.location.href = "../user/login_page";
    });
  }
});
