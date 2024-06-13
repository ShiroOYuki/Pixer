$(document).ready(() => {
  const form = document.getElementById("update-form");

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    const uid = getCookie("uid");
    const session_id = getCookie("session_id");

    const old_password = document.getElementById("old_password").value;
    const new_username = document.getElementById("new_username").value;
    const new_email = document.getElementById("new_email").value;
    const new_password = document.getElementById("new_password").value;

    const csrftoken = getCookie("csrftoken");

    // 驗證電子郵件格式
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    //驗證密碼格式
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/;

    const data = {
      uid: uid,
      session_id: session_id,
      old_password: old_password,
    };

    if (new_username) {
      data.username = new_username;
    }

    if (new_email) {
      if (!emailRegex.test(new_email)) {
        alert("請輸入有效的電子郵件地址");
        return;
      } else {
        data.email = new_email;
      }
    }

    if (new_password) {
      if (!passwordRegex.test(new_password)) {
        alert("密碼必須至少包含8個字符，包括大寫小寫字母、數字");
        return;
      } else {
        data.new_password = new_password;
      }
    }

    console.log("sending data: ", data);

    $.ajax({
      url: "http://127.0.0.1:8000/user/update",
      type: "POST",
      data: data,
      headers: { "X-CSRFToken": csrftoken },
      success: (res) => {
        console.log(res);

        window.location.href = "data_page";
      },
      error: (res) => {
        alert("Password Incorrect");
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
