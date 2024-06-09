$(document).ready(() => {
  const csrftoken = getCookie("csrftoken");

  const uid = getCookie("uid");
  const session_id = getCookie("session_id");

  const data = {
    uid: uid,
    session_id: session_id,
    targets: ["uid", "username", "email", "last_login", "create_time"],
  };

  const pixel = {
    uid: uid,
    session_id: session_id,
  };

  $.ajax({
    url: "http://127.0.0.1:8000/user/data",
    type: "POST",
    data: data,
    headers: { "X-CSRFToken": csrftoken },
    success: (res) => {
      console.log(res);

      $("#uid").val(res.uid);
      $("#username").val(res.username);
      $("#email").val(res.email);
      $("#last_login").val(res.last_login);
      $("#create_time").val(res.create_time);
    },
    error: (res) => {
      console.error("Error", res);
    },
  });
  $.ajax({
    url: "http://127.0.0.1:8000/user/wallet/get",
    type: "POST",
    data: data,
    headers: { "X-CSRFToken": csrftoken },
    success: (res) => {
      console.log(res);

      $("#pixel").val(res.pixel);
    },
    error: (res) => {
      console.error("Error", res);
    },
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
