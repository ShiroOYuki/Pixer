$(document).ready(() => {
  const form = document.getElementById("login-form");

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    const email = document.getElementById("user_email").value;
    const password = document.getElementById("password").value;

    const csrftoken = getCookie("csrftoken");

    const data = {
      email: email,
      password: password,
    };

    $.ajax({
      url: "http://127.0.0.1:8000/user/login",
      type: "POST",
      data: data,
      headers: { "X-CSRFToken": csrftoken },
      success: (res) => {
        console.log(res);

        const uid = res.uid;
        const session_id = res.session_id;

        setCookie("uid", uid, 7); // Cookie 有效期为 7 天
        setCookie("session_id", session_id, 7);

        console.log("Cookies set: ", document.cookie);

        window.location.href = "../homepage";
      },
      error: (res) => {
        console.error("Error", res);
      },
    });
  });
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

function setCookie(name, value, days) {
  let expires = "";
  if (days) {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}
