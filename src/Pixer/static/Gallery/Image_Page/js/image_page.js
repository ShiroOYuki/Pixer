// 替換成實際的 image_id 和 uid
/*const image_id = "46901bfa-62c1-48b3-8a44-7dc45e209e86";
const uid = getCookie("uid");

$.ajax({
  url: `/gallery/image/<${image_id}>/?uid=<${uid}>`,
  //data: { uid: uid },
  success: function (data) {
    $("#title").text(data.title);
    $("#image").attr("src", data.filepath);
    $("#description").text(data.description);
    $("#uploaded_by").text(
      `Uploaded by ${data.username} on ${data.create_time}`
    );
    $("#format").text(`Format: ${data.format}`);
    $("#download_times").text(`Downloaded ${data.download_times} times`);
    $("#favorite_status").text(
      data.is_favorite
        ? "This image is in your favorites."
        : "This image is not in your favorites."
    );
  },
  error: function (error) {
    console.error("Error:", error);
  },
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
*/
