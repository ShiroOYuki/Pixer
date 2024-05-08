from PIL import Image, ImageShow
from typing import Literal
import os

class ImageProcesser:
        
    def byte_to_image(self, img_data: bytes, size: tuple[int, int]):
        img = Image.frombuffer("RGB", size, img_data, "raw")
    
    def process(self, image: Image, channels: Literal[8, 16, 24], color_mode: Literal["gray", "rgb"], pixel_scale: int):
        image.convert()
        
if __name__ == "__main__":
    img = Image.open(r"C:\Users\bfkam\Downloads\GM1X0CSboAArOs2.jpg")
    ImageShow.show(img)
    
    print(img)