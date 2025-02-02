from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseServerError, HttpRequest

import time
import os
import datetime

from Pixelate import tests
from Pixelate.ImageProcesser import ImageProcesser
from Gallery.models import PixerImages
from User.models import PixerUser, PixerWallet
from libs.utils.UserTools import generate_session_id
from PIL import Image

# Create your views here.
def index(request):
    return HttpResponse("Hello Pixelate!")

def process_image(request: HttpRequest):
    if request.method == "POST":
        img_buf = request.FILES.get("image")
        mode = request.POST.get("mode")
        scale = request.POST.get("scale")
        channels = request.POST.get("channels")
        uid = request.POST.get("uid")
        img_format = request.POST.get("format")

        if uid is None: return HttpResponseBadRequest("key `uid` is required")
        if img_buf is None: return HttpResponseBadRequest("key `image` is required")
        if mode is None: return HttpResponseBadRequest("key `mode` is required")
        if scale is None: return HttpResponseBadRequest("key `scale` is required")
        if channels is None: return HttpResponseBadRequest("key `channels` is required")
        if img_format is None: return HttpResponseBadRequest("key `format` is required")
        
        scale = int(scale)
        channels = int(channels)
        
        ip = ImageProcesser()
        
        img_ary, size = ip.file_to_image(img_buf.read())
        
        if img_ary is None: return HttpResponseServerError("unknown error")

        process_res = ip.process(img_ary, channels, mode, scale)
        if process_res.code == 400: return HttpResponseBadRequest(process_res.msg)
        if process_res.code == 500: return HttpResponseServerError("unknown error")
        
        timestamp = str(time.time()).replace(".", "")
        filepath = ip.save(process_res, f"{uid}_{timestamp}.{img_format}")
            
        res = {"filepath": filepath}
        return JsonResponse(res, safe=False)
    
    return redirect("/pixelate")

def upload_gallery(request):
    if request.method == "POST":
        image_path = request.POST.get("filepath")
        uid = request.POST.get("uid")
        session_id = request.POST.get("session_id")
        title = request.POST.get("title")
        desc = request.POST.get("description")
        
        if image_path is None: return HttpResponseBadRequest("key `filepath` is required")
        if uid is None: return HttpResponseBadRequest("key `uid` is required")
        if session_id is None: return HttpResponseBadRequest("key `session_id` is required")
        
        if not os.path.exists(image_path): return HttpResponseBadRequest("filepath not exists")
        if title is None: title = "noname"
        
        is_login, _, _ = PixerUser.user_validation(uid, session_id)
        if not is_login: return HttpResponseBadRequest("validation failed")
        
        image_format = image_path.split(".")[-1]
        create_time = datetime.datetime.now()
        while True:
            image_id = generate_session_id()
            if not PixerImages.objects.filter(image_id=image_id).exists(): 
                break
            
        w, h = ImageProcesser.get_size(image_path)
        
        PixerImages.objects.create(
            image_id=image_id,
            uid=uid,
            filepath=image_path,
            create_time=create_time,
            format=image_format,
            download_times=0,
            title=title,
            description=desc,
            height=h,
            width=w
        )
        
        PixerWallet.change_pixel(uid, "upload")
        
        return JsonResponse({
            "image_id": image_id,
            "link_url": f"/gallery/image/{image_id}"
        })
    
    return redirect("/pixelate")

def test(request):
    tests.test_pixelate()
    tests.test_client_request()
    return HttpResponse("test")

def pixelate(request):
    return render(request, "pixelate.html")

def upload(request):
    return render(request, "upload_gallery.html")