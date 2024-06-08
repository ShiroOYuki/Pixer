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
    const scale = parseInt(document.getElementById("scale").value);
    const channels = parseInt(document.getElementById("channels").value);
    const format = document.getElementById("format").value;

    const file = imageInput.files[0];
    const reader = new FileReader();

    reader.onload = function (event) {
      const arrayBuffer = event.target.result;
      const byteArray = new Uint8Array(arrayBuffer);
      let binaryString = "";
      for (let i = 0; i < byteArray.length; i++) {
        binaryString += String.fromCharCode(byteArray[i]);
      }
      const imageData = btoa(binaryString); // 使用 base64 编码

      const img = new Image();
      img.src = URL.createObjectURL(file);
      img.onload = function () {
        const formDataObject = {
          uid: uid,
          image: imageData, // 以字符串形式传递图像数据
          size: [img.height, img.width],
          mode: mode,
          scale: scale,
          channels: channels,
          format: format,
        };

        $.ajax({
          url: "http://127.0.0.1:8000/pixelate/upload",
          type: "POST",
          data: formDataObject,
          processData: false,
          headers: { "X-CSRFToken": csrftoken },
          success: (res) => {
            console.log(res);
            window.location.href = "#";
          },
          error: (res) => {
            console.log(formDataObject);
            console.error("Error", res);
          },
        });
      };
    };
    reader.readAsArrayBuffer(file);
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
