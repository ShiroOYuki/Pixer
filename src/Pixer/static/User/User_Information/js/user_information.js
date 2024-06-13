$(document).ready(() => {
  $("#btnSignout-popup").click(function (event) {
    event.preventDefault(); // 阻止默认行为

    // 清除 uid 和 session_id cookie
    document.cookie = "uid=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.cookie =
      "session_id=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

    // 页面重定向到登出页面
    window.location.href = $(this).attr("href");
  });

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
      $("#pixel").val(Math.round(res.pixel * 10) / 10);
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
