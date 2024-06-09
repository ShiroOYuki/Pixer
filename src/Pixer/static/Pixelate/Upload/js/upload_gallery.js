document.addEventListener("DOMContentLoaded", function () {
  // 動態載入圖片的路徑
  const imagePath =
    "{% static 'Pixelate/imgs/temps/81fe69d53c35c7e70724_17179452035731351.png' %}";
  document.getElementById("image").src = imagePath;
});
