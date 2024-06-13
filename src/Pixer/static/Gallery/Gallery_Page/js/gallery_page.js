$(document).ready(async () => {
  const csrftoken = getCookie("csrftoken");
  let firstload = true;
  let imageIndex;
  let column;
  let columns_height;
  let columns_x;

  async function fetchImages(page, limit) {
    return new Promise((resolve, reject) => {
      const data = {
        page: page,
        limit: limit,
      };
      $.ajax({
        url: "http://127.0.0.1:8000/gallery/page",
        type: "POST",
        data: data,
        headers: { "X-CSRFToken": csrftoken },
        success: (res) => {
          resolve(res); // 成功時解析數據
        },
        error: (res) => {
          console.error("Error", res);
          reject(res); // 失敗時拒絕數據
        },
      });
    });
  }

  async function displayImages() {
    try {
      await fetchImages(1, 30).then((images) => calc_height(images)); // 等待 Promise 解析數據
    } catch (error) {
      console.error("Failed to display images", error);
    }
  }

  document.addEventListener("DOMContentLoaded", displayImages);

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

  function calc_height(images) {
    console.log(images);
    // let max_item_height = 400; // 測試用元件的最大高度
    // let min_item_height = 100; // 測試用元件的最小高度

    let item_w = 400; // 元件寬度
    let gap = 20; // 元件與元件之間的間隔
    let total_w = document.getElementById("out-container").clientWidth; // container 總寬度
    column = Math.floor(total_w / (item_w + 10)); // 計算以現在的 container 寬度來說，可以塞幾排

    let container = document.createElement("div"); // 等等元件會插入到這個元素
    container.className = "container";
    let container_w = (item_w + gap) * column - gap;
    container.style.minWidth = container_w + "px";
    document.getElementById("out-container").appendChild(container);
    if (firstload) {
      columns_height = new Array(column).fill(0); // 每排的高度 (y)
      columns_x = new Array(column).fill(0); // 每排元素的橫軸要從哪裡開始 (x)

      // 初始化 columns_x
      for (let i = 0; i < column; i++) {
        columns_x[i] = (item_w + gap) * i;
      }
      imageIndex = 0;
      firstload = false;
    }

    images.forEach((image) => {
      let column_now = columns_height.indexOf(Math.min(...columns_height));
      const imgDiv = document.createElement("div");
      imgDiv.classList.add("image_container");
      imgDiv.className = "box";
      imgDiv.style.transform =
        "translateX(" +
        columns_x[column_now].toString() +
        "px) translateY(" +
        columns_height[column_now].toString() +
        "px)";

      const imgElement = document.createElement("img");
      const image_path = image.filepath;

      if (image_path) {
        let searchString = "/static"; //刪除static前面的path
        let indexString = image_path.indexOf(searchString);

        if (indexString !== -1) {
          let showPath = image_path.substring(indexString); //for review the result
          imgElement.src = showPath;
        } else {
          console.log("Trimmed path error");
        }
      } else {
        console.log("Receive path error");
      }

      imgElement.alt = image.image_id;
      imgElement.addEventListener("click", () => {
        window.location.href =
          "/gallery/image/" + image.image_id + "?uid=" + getCookie("uid");
      });
      imgDiv.appendChild(imgElement);
      container.appendChild(imgDiv);

      columns_height[column_now] += 400 + gap;
      imageIndex += 1;
    });
  }
  await displayImages();
});
