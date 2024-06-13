document.addEventListener("DOMContentLoaded", () => {
  console.log("Homepage script loaded!");
  const csrftoken = getCookie("csrftoken");

  // Smooth scrolling for links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const targetId = this.getAttribute("href").substring(1); // Remove the '#' character
      const targetElement = document.getElementById(targetId);
      if (targetElement) {
        targetElement.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  const data = {
    page: 1,
    limit: 3,
  };
  $.ajax({
    url: "http://127.0.0.1:8000/gallery/page",
    type: "POST",
    data: data,
    headers: { "X-CSRFToken": csrftoken },
    success: (res) => {
      let imageStyle = "";
      res.forEach((image) => {
        imagePath = trimmedPath(image.filepath, "/static");
        imageStyle += "url(" + imagePath + "),";
      });
      imageStyle = imageStyle.slice(0, -1);
      console.log(document.getElementById("hero"));
      document.getElementById("hero").style.backgroundImage = imageStyle;
    },
    error: (res) => {
      console.error("Error", res);
      reject(res); // 失敗時拒絕數據
    },
  });
});

function trimmedPath(fullPath, target) {
  if (fullPath) {
    let indexString = fullPath.indexOf(target);

    if (indexString !== -1) {
      let showPath = fullPath.substring(indexString); //for review the result
      return showPath;
    } else {
      console.log("Trimmed path error");
    }
  } else {
    console.log("Receive path error");
  }
  return null;
}

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
