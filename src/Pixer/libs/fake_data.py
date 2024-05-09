from PIL import Image

class Fake:

    def get_byte_image() -> bytes:
        img = Image.open(r"D:\OneDrive\圖片\桌布\ancient-pagoda-stands-tall-autumn-forest-generated-by-ai2.jpg")
        img_format = img.format
        img = img.convert("RGB")
        size = img.size
        img_buf = img.tobytes()
        
        return {
            "image": img_buf, 
            "size": size
        }