from PIL import Image
from typing import Literal, Optional
import numpy as np
import os
import io

class PixelateResultType:
    def __init__(self, image: Optional[np.ndarray], code: int, msg: str):
        self.image = image
        self.code = code
        self.msg = msg

class ImageProcesser:
    def file_to_image(self, img_data: bytes):
        img_ary = None
        try:
            img_data = io.BytesIO(img_data)
            img = Image.open(img_data)
            size = img.size
            img_ary = np.array(img)
            img_ary = img_ary.reshape((size[1], size[0], 3))
        except Exception as e:
            print(e)
        return img_ary, img.size
    
    def process(self, image: np.ndarray, channels: Literal[6, 12, 24], color_mode: Literal["gray", "rgb"], pixel_scale: int) -> PixelateResultType:
        res = None
        code = 500
        msg = "Internal Server Error"
        try:
            size = image.shape
            scale = 2**(channels/3)-1
            
            if color_mode == "rgb" or color_mode == "gray":
                res = np.ndarray(size, dtype=np.uint8)
                for row in range(0, size[0], pixel_scale):
                    for col in range(0, size[1], pixel_scale):
                        r = round(np.mean(image[row:row+pixel_scale, col:col+pixel_scale, 0])/255*scale)/scale * 255
                        g = round(np.mean(image[row:row+pixel_scale, col:col+pixel_scale, 1])/255*scale)/scale * 255
                        b = round(np.mean(image[row:row+pixel_scale, col:col+pixel_scale, 2])/255*scale)/scale * 255
                        if color_mode == "rgb":
                            res[row:row+pixel_scale, col:col+pixel_scale, 0] = r
                            res[row:row+pixel_scale, col:col+pixel_scale, 1] = g
                            res[row:row+pixel_scale, col:col+pixel_scale, 2] = b
                        else:
                            gray = np.mean((r, g, b))
                            res[row:row+pixel_scale, col:col+pixel_scale, 0] = gray
                            res[row:row+pixel_scale, col:col+pixel_scale, 1] = gray
                            res[row:row+pixel_scale, col:col+pixel_scale, 2] = gray
                code = 200
                msg = "OK"
            else:
                code = 400
                msg = f"Color mode '{color_mode}' is unsupported."
        except Exception as e: 
            print(e)
            
        return PixelateResultType(res, code, msg)
        
    def save(self, data: PixelateResultType, filename: str):
        img_res = data.image
        img = Image.fromarray(img_res)
        # 确保目录存在
        directory = os.path.join(os.getcwd(), "static", "Pixelate", "imgs", "temps")
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = os.path.join(directory, filename)
        img.save(filepath)
        return filepath
    
    @classmethod
    def get_size(self, filepath: str):
        img = Image.open(filepath)
        return img.size
                
        
        
