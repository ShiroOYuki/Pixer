document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector(".register-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault(); // 防止表單提交，進行自訂驗證

    const username = document.getElementById("user_name").value;
    const email = document.getElementById("user_email").value;
    const password = document.getElementById("password").value;

    // 驗證電子郵件格式
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert("請輸入有效的電子郵件地址");
      return;
    }

    //驗證密碼格式
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!passwordRegex.test(password)) {
      alert("密碼必須至少包含8個字符，包括大寫小寫字母、數字");
      return;
    }

    const csrftoken = getCookie("csrftoken");

    const data = {
      username: username,
      email: email,
      password: password,
    };

    $.ajax({
      url: "http://127.0.0.1:8000/user/create",
      type: "POST",
      data: data,
      headers: { "X-CSRFToken": csrftoken },
      success: (res) => {
        console.log(res);
        window.location.href = "#";
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
