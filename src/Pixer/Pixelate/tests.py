import os
from django.test import TestCase
import numpy as np
from PIL import Image
import time
from Pixelate.ImageProcesser import ImageProcesser
from libs.fake_data import Fake

class AutoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        img_path = "./static/Pixelate/imgs/test/test.jpg"
        scale = 8
        cls.ip = ImageProcesser()
        cls.get_data = lambda mode, channels: Fake.get_byte_image(
            img_path=img_path,
            mode=mode,
            scale=scale,
            channels=channels,
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

    # 其他测试函数保持不变...

def test_pixelate():
    ip = ImageProcesser()
    img_data = Fake.get_byte_image(
        img_path="./static/Pixelate/imgs/test/test.jpg",
        mode="rgb",
        scale=8,
        channels=24
    )

    img_buf = img_data["image"]
    size = img_data["size"]
    mode = img_data["mode"]
    scale = img_data["scale"]

    img_ary = ip.byte_to_image(img_buf, (size[1], size[0], 3))
    if img_ary is None:
        return

    # 保存结果图片
    results_path = "./static/Pixelate/imgs/test/result"
    if not os.path.exists(results_path):
        os.makedirs(results_path)

    # 24-bit
    img_res = ip.process(img_ary, 24, mode, scale)
    img_res = img_res.image
    img = Image.fromarray(img_res)
    img.save(os.path.join(results_path, "24-bit.png"))

    # 12-bit
    img_res = ip.process(img_ary, 12, mode, scale)
    img_res = img_res.image
    img = Image.fromarray(img_res)
    img.save(os.path.join(results_path, "12-bit.png"))

    # 6-bit
    img_res = ip.process(img_ary, 6, mode, scale)
    img_res = img_res.image
    img = Image.fromarray(img_res)
    img.save(os.path.join(results_path, "6-bit.png"))

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
    filename = f"{uid}_{timestamp}.{img_format}"
    filepath = ip.save(process_res, filename)
    res = {
        "filepath": filepath,
        "code": process_res.code,
        "msg": process_res.msg
    }
    print(res)
