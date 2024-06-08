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
    const image = imageInput.files[0];
    const mode = document.getElementById("mode").value;
    const scale = document.getElementById("scale").value;
    const channels = document.getElementById("channels").value;
    const format = document.getElementById("format").value;

    const img = new Image();
    img.src = URL.createObjectURL(image);
    img.onload = function () {
      // 定义一个包含所有表单数据的对象
      const formDataObject = {
        uid: uid,
        image: image,
        size: JSON.stringify([img.height, img.width]),
        mode: mode,
        scale: scale,
        channels: channels,
        format: format,
      };

      // 创建FormData对象并填充数据
      const formData = new FormData();
      Object.keys(formDataObject).forEach((key) => {
        formData.append(key, formDataObject[key]);
      });

      $.ajax({
        url: "http://127.0.0.1:8000/pixerlate/upload",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        headers: { "X-CSRFToken": csrftoken },
        success: (res) => {
          console.log(res);
          window.location.href = "#";
        },
        error: (res) => {
          console.log(formData);
          console.error("Error", res);
        },
      });
    };
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
