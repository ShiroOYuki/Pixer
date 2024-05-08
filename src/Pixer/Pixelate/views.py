from django.shortcuts import render
from django.http import HttpResponse

import cv2

from Pixelate.ImageProcesser import ImageProcesser
from libs.fake_data import Fake

# Create your views here.
def index(request):
    return HttpResponse("Hello Pixelate!")

def test(request):
    ip = ImageProcesser()
    
    img_data = Fake.get_byte_image()
    img_buf, size = img_data["image"], img_data["size"]
    img_ary = ip.byte_to_image(img_buf, (size[1], size[0], 3))
    
    img_res = ip.process(img_ary, 24, 'rgb', 8)
    
    cv2.imshow("Original", img_ary[:, :, ::-1])
    cv2.waitKey(0)
    
    cv2.imshow("24-bit pixel", img_res[:, :, ::-1])
    cv2.waitKey(0)
    
    img_res = ip.process(img_ary, 12, 'rgb', 8)
    cv2.imshow("12-bit pixel", img_res[:, :, ::-1])
    cv2.waitKey(0)
    
    img_res = ip.process(img_ary, 6, 'rgb', 8)
    cv2.imshow("6-bit pixel", img_res[:, :, ::-1])
    cv2.waitKey(0)
    
    img_res = ip.process(img_ary, 3, 'rgb', 8)
    cv2.imshow("3-bit pixel", img_res[:, :, ::-1])
    cv2.waitKey(0)
    
    return HttpResponse("test")