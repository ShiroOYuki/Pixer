from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseServerError

import time

from Pixelate import tests
from Pixelate.ImageProcesser import ImageProcesser

# Create your views here.
def index(request):
    return HttpResponse("Hello Pixelate!")

def process_image(request):
    if request.method == "POST":
        img_buf = request.POST.get("image")
        size = request.POST.get("size")
        mode = request.POST.get("mode")
        scale = request.POST.get("scale")
        channels = request.POST.get("channels")
        uid = request.POST.get("uid")
        img_format = request.POST.get("format")
        
        if uid is None: return HttpResponseBadRequest("key `uid` is required")
        if img_buf is None: return HttpResponseBadRequest("key `image` is required")
        if size is None: return HttpResponseBadRequest("key `size` is required")
        if mode is None: return HttpResponseBadRequest("key `mode` is required")
        if scale is None: return HttpResponseBadRequest("key `scale` is required")
        if channels is None: return HttpResponseBadRequest("key `channels` is required")
        if img_format is None: return HttpResponseBadRequest("key `format` is required")
        
        ip = ImageProcesser()
        
        img_ary = ip.byte_to_image(img_buf, (size[1], size[0], 3))
        if img_ary is None: return HttpResponseServerError("unknown error")
            
        process_res = ip.process(img_ary, channels, mode, scale)
        
        if process_res.code == 400: return HttpResponseBadRequest(process_res.msg)
        if process_res.code == 500: return HttpResponseServerError("unknown error")
        
        timestamp = str(time.time()).replace(".", "")
        filepath = ip.save(process_res, f"{uid}_{timestamp}.{img_format}")
            
        res = {"filepath": filepath,}
        return JsonResponse(res, safe=False)
    
    return redirect("/pixelate")

def test(request):
    tests.test_pixelate()
    tests.test_client_request()
    return HttpResponse("test")

def pixelate(request):
    return render(request, "pixelate.html")