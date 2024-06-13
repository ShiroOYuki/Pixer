$(document).ready(() => {
  console.log(is_Favorite);
  const iconElement = document.querySelector(".bookmarks-outline ion-icon");
  if (is_Favorite == "True") {
    iconElement.setAttribute("name", "bookmarks");
  } else {
    iconElement.setAttribute("name", "bookmarks-outline");
  }

  const data = {
    uid: getCookie("uid"),
    session_id: getCookie("session_id"),
    image_id: imageId,
  };
  const csrftoken = getCookie("csrftoken");
  $(".toggle-download .bookmarks-outline ion-icon").on("click", function () {
    $.ajax({
      url: "http://127.0.0.1:8000/gallery/toggle-favorite",
      type: "POST",
      data: data,
      headers: { "X-CSRFToken": csrftoken },
      success: (res) => {
        console.log(res);
        location.reload();
      },
      error: (res) => {
        console.error("Error", res);
      },
    });
  });

  $(".toggle-download > ion-icon[name='download-outline']").on(
    "click",
    function () {
      $.ajax({
        url: "http://127.0.0.1:8000/gallery/download",
        type: "POST",
        data: data,
        headers: { "X-CSRFToken": csrftoken },
        success: (res) => {
          console.log(res);
          const a = document.createElement("a");
          a.style.display = "none";
          a.href = trimmedPath(filePath, "/static");
          a.download = a.href;
          a.click();
          location.reload();
        },
        error: (res) => {
          console.error("Error", res);
        },
      });
      $(this).toggleClass("download-active");
    }
  );
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
