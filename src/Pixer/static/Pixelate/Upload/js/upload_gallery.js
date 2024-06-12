document.addEventListener("DOMContentLoaded", function () {
  let image_path = localStorage.getItem("Image_Path");
  const uploadButton = document.getElementById("btnUpload-popup");
  let sendPath;

  if (image_path) {
    let searchSymbols = ".png"; //刪除path後面的"}
    let searchString = "/static"; //刪除static前面的path
    let searchLabel = '"filepath":"';
    let indexSymbols = image_path.indexOf(searchSymbols);
    let indexString = image_path.indexOf(searchString);
    let indexPath = image_path.indexOf(searchLabel);

    if (indexSymbols !== -1) {
      let trimmedPath = image_path.substring(
        0,
        indexSymbols + searchSymbols.length
      );
      let showPath = trimmedPath.substring(indexString); //for review the result
      sendPath = trimmedPath.substring(indexPath + searchLabel.length); //要傳送給後端的path

      document.getElementById("result_image").src = showPath;
    } else {
      console.log("Trimmed path error");
    }
  } else {
    console.log("Receive path error");
  }

  uploadButton.addEventListener("click", (event) => {
    event.preventDefault();

    const csrftoken = getCookie("csrftoken");
    const uid = getCookie("uid");
    const session_id = getCookie("session_id");

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    const data = {
      uid: uid,
      session_id: session_id,
      filepath: sendPath,
      title: title,
      description: description,
    };

    console.log(data);

    $.ajax({
      url: "http://127.0.0.1:8000/pixelate/upload-gallery",
      type: "POST",
      data: data,
      headers: { "X-CSRFToken": csrftoken },
      success: (res) => {
        console.log(res);

        window.location.href = res.link_url + "?uid=" + uid;
      },
      error: (res) => {
        console.error("Error", res);
      },
    });
  });
});

function setCookie(name, value, days) {
  let expires = "";
  if (days) {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}
