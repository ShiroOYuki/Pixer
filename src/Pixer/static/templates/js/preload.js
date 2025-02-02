$(document).ready(() => {
  var user_icon = document.getElementById("user-icon");
  var btnLogin_popup = document.getElementById("btnLogin-popup");

  if (getCookie("uid") && getCookie("session_id")) {
    user_icon.style.display = "block";
    btnLogin_popup.style.display = "none";
  }
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
