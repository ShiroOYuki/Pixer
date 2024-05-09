from PIL import Image

class Fake:
    def get_byte_image(img_path, mode="rgb", scale=8, channels=24, img_format="png") -> bytes:
        img = Image.open(img_path)
        img = img.convert("RGB")
        size = img.size
        img_buf = img.tobytes()
        
        return {
            "uid": "test_uid",
            "image": img_buf, 
            "size": size,
            "mode": mode,
            "scale": scale,
            "channels": channels,
            "format": img_format
        }