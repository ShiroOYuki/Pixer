document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("upload-form");
  const imageInput = document.getElementById("image");
  const imagePreview = document.getElementById("image-preview");

  imageInput.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (event) {
        imagePreview.src = event.target.result;
        imagePreview.style.display = "block";
      };
      reader.readAsDataURL(file);
    } else {
      imagePreview.src = "";
      imagePreview.style.display = "none";
    }
  });

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const csrftoken = getCookie("csrftoken");
    const uid = getCookie("uid");
    const mode = document.getElementById("mode").value;
    const scale = document.getElementById("scale").value;
    const channels = document.querySelector(
      'input[name="channels"]:checked'
    ).value;
    const format = document.getElementById("format").value;

    const file = imageInput.files[0];

    const formData = new FormData();

    formData.append("uid", uid);
    formData.append("image", file);
    formData.append("mode", mode);
    formData.append("scale", scale);
    formData.append("channels", channels);
    formData.append("format", format);

    for (const [key, value] of formData.entries()) {
      console.log(`${key}: ${value}`);
    }

    $.ajax({
      url: "http://127.0.0.1:8000/pixelate/upload",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      headers: { "X-CSRFToken": csrftoken },
      success: (res) => {
        console.log(res);
        localStorage.setItem("Image_Path", JSON.stringify(res));
        window.location.href = "upload_page";
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
});
