from django.test import TestCase

import cv2
import numpy as np
from PIL import Image
import time

from Pixelate.ImageProcesser import ImageProcesser
from libs.fake_data import Fake


# Create your tests here.
# https://docs.djangoproject.com/en/5.0/topics/testing/overview/

class AutoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        img_path ="./static/Pixelate/imgs/test/test.jpg"
        scale = 8
        cls.ip = ImageProcesser()
        cls.get_data = lambda mode, channels: Fake.get_byte_image(
            img_path = img_path,
            mode = mode,
            scale = scale,
            channels = channels,
        )
        
    def test_pixelate_rgb_24(self):
        img_data = self.get_data("rgb", 24)
        
        img_buf = img_data["image"]
        size = img_data["size"]
        mode = img_data["mode"]
        scale = img_data["scale"]
        channels = img_data["channels"]
        
        img_ary = self.ip.byte_to_image(img_buf, (size[1], size[0], 3))
        
        img_res = self.ip.process(img_ary, channels, mode, scale)
        self.assertEqual(img_res.code, 200)
        self.assertEqual(type(img_res.image), np.ndarray)
        
        
    def test_pixelate_rgb_12(self):
        img_data = self.get_data("rgb", 12)
        
        img_buf = img_data["image"]
        size = img_data["size"]
        mode = img_data["mode"]
        scale = img_data["scale"]
        channels = img_data["channels"]
        
        img_ary = self.ip.byte_to_image(img_buf, (size[1], size[0], 3))
        
        img_res = self.ip.process(img_ary, channels, mode, scale)
        self.assertEqual(img_res.code, 200)
        self.assertEqual(type(img_res.image), np.ndarray)
        
        
    def test_pixelate_rgb_6(self):
        img_data = self.get_data("rgb", 6)
        
        img_buf = img_data["image"]
        size = img_data["size"]
        mode = img_data["mode"]
        scale = img_data["scale"]
        channels = img_data["channels"]
        
        img_ary = self.ip.byte_to_image(img_buf, (size[1], size[0], 3))
        
        img_res = self.ip.process(img_ary, channels, mode, scale)
        self.assertEqual(img_res.code, 200)
        self.assertEqual(type(img_res.image), np.ndarray)
        
        
    def test_pixelate_gray_24(self):
        img_data = self.get_data("gray", 24)
        
        img_buf = img_data["image"]
        size = img_data["size"]
        mode = img_data["mode"]
        scale = img_data["scale"]
        channels = img_data["channels"]

        img_ary = self.ip.byte_to_image(img_buf, (size[1], size[0], 3))
        
        img_res = self.ip.process(img_ary, channels, mode, scale)
        self.assertEqual(img_res.code, 200)
        self.assertEqual(type(img_res.image), np.ndarray)
        
    def test_pixelate_gray_12(self):
        img_data = self.get_data("gray", 12)
        
        img_buf = img_data["image"]
        size = img_data["size"]
        mode = img_data["mode"]
        scale = img_data["scale"]
        channels = img_data["channels"]

        img_ary = self.ip.byte_to_image(img_buf, (size[1], size[0], 3))
        
        img_res = self.ip.process(img_ary, channels, mode, scale)
        self.assertEqual(img_res.code, 200)
        self.assertEqual(type(img_res.image), np.ndarray)
        
    def test_pixelate_gray_6(self):
        img_data = self.get_data("gray", 6)
        
        img_buf = img_data["image"]
        size = img_data["size"]
        mode = img_data["mode"]
        scale = img_data["scale"]
        channels = img_data["channels"]

        img_ary = self.ip.byte_to_image(img_buf, (size[1], size[0], 3))
        
        img_res = self.ip.process(img_ary, channels, mode, scale)
        self.assertEqual(img_res.code, 200)
        self.assertEqual(type(img_res.image), np.ndarray)
        
def test_pixelate():
    ip = ImageProcesser()
    
    img_data = Fake.get_byte_image(
        img_path = "./static/Pixelate/imgs/test/test.jpg",
        mode = "rgb",
        scale = 8,
        channels = 24
    )
    
    img_buf = img_data["image"]
    size = img_data["size"]
    mode = img_data["mode"]
    scale = img_data["scale"]
    
    img_ary = ip.byte_to_image(img_buf, (size[1], size[0], 3))
    
    if img_ary is None: return
    
    # Original
    cv2.imshow("Original", img_ary[:, :, ::-1])
    cv2.waitKey(0)
    
    # 24-bit
    img_res = ip.process(img_ary, 24, mode, scale)
    img_res = img_res.image
    # cv2.imshow("24-bit pixel", img_res[:, :, ::-1])
    # cv2.waitKey(0)
    img = Image.fromarray(img_res)
    img.save("./static/Pixelate/imgs/test/result/24-bit.png")
    
    # 12-bit
    img_res = ip.process(img_ary, 12, mode, scale)
    img_res = img_res.image
    # cv2.imshow("12-bit pixel", img_res[:, :, ::-1])
    # cv2.waitKey(0)
    img = Image.fromarray(img_res)
    img.save("./static/Pixelate/imgs/test/result/12-bit.png")
    
    # 6-bit
    img_res = ip.process(img_ary, 6, mode, scale)
    img_res = img_res.image
    # cv2.imshow("6-bit pixel", img_res[:, :, ::-1])
    # cv2.waitKey(0)
    img = Image.fromarray(img_res)
    img.save("./static/Pixelate/imgs/test/result/6-bit.png")
    
def test_client_request():
    ip = ImageProcesser()
    img_data = Fake.get_byte_image("./static/Pixelate/imgs/test/test.jpg")
    
    uid = img_data["uid"]
    img_buf = img_data["image"]
    size = img_data["size"]
    mode = img_data["mode"]
    scale = img_data["scale"]
    channels = img_data["channels"]
    img_format = img_data["format"]
    
    img_ary = ip.byte_to_image(img_buf, (size[1], size[0], 3))
    process_res = ip.process(img_ary, channels, mode, scale)
    
    timestamp = str(time.time()).replace(".", "")
    filepath = ip.save(process_res, f"{uid}_{timestamp}.{img_format}")
    res = {
            "filepath": filepath,
            "code": process_res.code,
            "msg": process_res.msg
    }
    print(res)
    
    