# Pixer

## 開發注意

### 建置

> 需要 Python 3.11.X

1. git 抓下來
2. run `cd Pixer`
3. run `virtualenv .pixer_venv --python=python3.11`
4. run `.pixer_venv/Script/activate`
5. run `pip install -r req.txt`
6. run `cd src\Pixer`
7. run `manage.py runserver`

### for MacOS

1. git 抓下來
2. run `cd Pixer`
3. run `virtualenv .pixer_venv --python=python3.11`
4. run `. ./.pixer_venv/Script/activate`
5. run `pip install -r req.txt`
6. run `cd src\Pixer`
7. run `python manage.py runserver`

### Git 注意事項

- 記得開 Branch，不要在 main 上面做修改
- 開發、Debug 完再 merge 到 main
- merge 完後，可以再用 main 開一個新的 Branch 繼續開發

### 檔案結構

```
Pixer
 ├─.pixer_venv                // Python 虛擬環境
 ├─src
 │  └─Pixer
 │     ├─Pixer                // Django 設定檔
 │     ├─Homepage             // 主頁
 │     ├─Pixelate             // 圖片轉像素圖的頁面
 │     ├─Gallery              // 畫廊
 │     ├─User                 // 使用者相關 (登入、設定、書籤)
 │     ├─libs                 // 各種工具函式檔案
 │     └─static               // 網頁會用到的各種檔案
 │        ├─Gallery           // 畫廊網頁檔案 (分頁，非模板/工具，所以用大寫開頭)
 │        │  ├─css            // 畫廊 css
 │        │  └─js             // 畫廊 js
 │        ├─Homepage
 │        │  ├─css
 │        │  └─js
 │        ├─Pixelate
 │        │  ├─css
 │        │  └─js
 │        ├─User
 │        │  ├─css
 │        │  └─js
 │        ├─templates         // 模板 (資料夾以小寫開頭)
 │        │  ├─css
 │        │  └─js
 │        ├─fonts             // 字形檔案
 │        └─imgs              // 各種圖片 (包含 icon)
 ├─README.md                  // 這份檔案
 ├─req.txt                    // Python 所需套件
 └─.git                       // Github 資料夾

```

### 命名規範

- Class 以駝峰式命名，且以大寫開頭，如：

  ```py
  # python
  class PixerTool:
      def __init__(self): ...
  ```

  ```js
  // js
  class PixerTool {
      constructor() {...}
  }
  ```

- def/function、變數以蛇底式命名，且以小寫開頭，如:

  ```py
  # python
  def one_plus_one():
      num_first = 1
      num_second = 1
      return num_first + num_second
  ```

  ```js
  // js
  function one_plus_one() {
    let num_first = 1;
    let num_second = 1;
    return num_first + num_second;
  }
  ```

- 常數以純大寫命名，如:

  ```py
  # python
  PI = 3.14
  DESKTOP_PATH = "C:/Desktop"
  ```

  ```js
  // js 不需使用大寫，但依舊使用小寫蛇底式命名
  const pi = 3.14;
  const desktop_path = "C:/Desktop";
  ```

## 介紹

### 功能

- 將圖片轉換為像素風格 (Pixel art style)
- 可選擇 8-bit、16-bit、24-bit 色彩
- 最小可至 16x16px 大小
- 有畫廊可以給你看別人生成的圖片
- 可自己選擇是否將生成的圖片發布
- 以書籤功能紀錄別人生成的圖片

### 點數機制

- Pixer 上的點數稱為 "像素 (Pixel)"
- 代表符號為 "■"，例如 "154 ■"
- 上傳一張生成出來的像素圖到畫廊可獲得 1 ■
- 下載一張別人創造的像素圖到畫廊需消耗 1 ■
- 每有一個人下載自己上傳的像素圖可獲得 0.1 ■

### 技術

- Python - Django、PIL
- HTML、CSS、JS
- SQL

### Test

1234567890-
