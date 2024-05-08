from PIL import Image, ImageShow
from typing import Literal
import cv2
import numpy as np
import io

class ImageProcesser:
    def byte_to_image(self, img_data: bytes, size: tuple[int, int, int]):
        img_ary = np.frombuffer(img_data, dtype=np.uint8).reshape(size)
        img_ary = img_ary.reshape(size)
        return img_ary
    
    def process(self, image: np.ndarray, channels: Literal[3, 6, 12, 24], color_mode: Literal["gray", "rgb"], pixel_scale: int):
        size = image.shape
        res = np.ndarray(size, dtype=np.uint8)
        scale = 2**(channels/3)-1
        
        for row in range(0, size[0], pixel_scale):
            for col in range(1, size[1], pixel_scale):
                r = round(np.mean(image[row:row+pixel_scale, col:col+pixel_scale, 0])/255*scale)/scale * 255
                g = round(np.mean(image[row:row+pixel_scale, col:col+pixel_scale, 1])/255*scale)/scale * 255
                b = round(np.mean(image[row:row+pixel_scale, col:col+pixel_scale, 2])/255*scale)/scale * 255
                res[row:row+pixel_scale, col:col+pixel_scale, 0] = r
                res[row:row+pixel_scale, col:col+pixel_scale, 1] = g
                res[row:row+pixel_scale, col:col+pixel_scale, 2] = b
        
        return res
                
        
        