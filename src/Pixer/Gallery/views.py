from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseServerError, HttpRequest


from libs.utils.GalleryTools import get_image_data
from libs.utils.UserTools import generate_session_id
from Gallery.models import PixerImages, PixerFavorites
from User.models import PixerUser, PixerWallet

# Create your views here.
def index(request):
    return HttpResponse("Hello Gallery!")

def image_page(request, image_id:str):
    uid = request.GET.get("uid") # 在網址後面接 ?uid=<your_uid>
    if uid == "": uid = None
    
    data = get_image_data(image_id, uid) # 回傳圖片的各種資料(參考 DB: pixer_images)
                                         # 並加上創建這張圖片的人的 username
                                         # (未製作): 以及是否已經在 favorite 裡面
                                    
    return JsonResponse(data, safe=False)       # 要導向到正確的頁面時，把這行註解
                                                # 然後把下面那行取消註解，將 html 改成正確的檔案
                                    
    # return render(request, "your_html_file.html", context=data)
    
def toggle_favorite(request):
    if request.method == "POST":
        uid = request.POST.get("uid")
        session_id = request.POST.get("session_id")
        image_id = request.POST.get("image_id")
        
        if uid is None: return HttpResponseBadRequest("key `uid` is required")
        if session_id is None: return HttpResponseBadRequest("key `session_id` is required")
        if image_id is None: return HttpResponseBadRequest("key `image_id` is required")
        
        is_login, _, _ = PixerUser.user_validation(uid, session_id)
        if not is_login: return HttpResponseBadRequest("validation failed")
        
        if not PixerImages.objects.filter(image_id=image_id).exists(): return HttpResponseBadRequest("gallery not exists")
        
        favorite_manager = PixerFavorites.objects.filter(uid=uid, image_id=image_id)
        
        if favorite_manager.exists():
            favorite_manager.delete()
        else:
            while True:
                favorite_id = generate_session_id()
                if not PixerFavorites.objects.filter(favorite_id=favorite_id).exists(): break
                
            PixerFavorites.objects.create(
                favorite_id=favorite_id,
                uid=uid,
                image_id=image_id
            )
        
        return HttpResponse("OK")
    
    return redirect("/gallery")

def get_page(request):
    if request.method == "POST":
        page = request.POST.get("page")
        limit = request.POST.get("limit")
        
        try:
            if page is None or not page.isdigit(): page = 1
            if limit is None or not limit.isdigit(): limit = 8
            
            page = int(page)
            limit = int(limit)
            
            start = limit * (page-1)
            end = start + limit
            
            data = list(PixerImages.objects.all().order_by("-create_time")[start:end].values())
        
            return JsonResponse(data, safe=False)
        except:
            return HttpResponseServerError("unknown error")
    return HttpResponseBadRequest("unsupported method")

def update_image_info(request):
    if request.method == "POST":
        uid = request.POST.get("uid")
        session_id = request.POST.get("session_id")
        image_id = request.POST.get("image_id")
        title = request.POST.get("title")
        desc = request.POST.get("description")
        
        if uid is None: return HttpResponseBadRequest("key `uid` is required")
        if session_id is None: return HttpResponseBadRequest("key `session_id` is required")
        if image_id is None: return HttpResponseBadRequest("key `image_id` is required")
        
        # validation
        if not PixerImages.check_is_author(image_id, uid): return HttpResponseBadRequest("permission denied")
        
        is_login, _, _ = PixerUser.user_validation(uid, session_id)
        if not is_login: return HttpResponseBadRequest("validation failed")
        
        try:
            image_manager = PixerImages.objects.filter(image_id=image_id)
            if title is None: title = image_manager.values().first().get("title")
            if desc is None: desc = image_manager.values().first().get("description")
            
            image_manager.update(
                title=title,
                description=desc
            )
            return HttpResponse("OK")
        except:
            return HttpResponseServerError("unknown error")
    
    return redirect("/gallery")

def remove_gallery(request):
    if request.method == "POST":
        uid = request.POST.get("uid")
        session_id = request.POST.get("session_id")
        image_id = request.POST.get("image_id")
        
        if uid is None: return HttpResponseBadRequest("key `uid` is required")
        if session_id is None: return HttpResponseBadRequest("key `session_id` is required")
        if image_id is None: return HttpResponseBadRequest("key `image_id` is required")
        
        
        
        # validation
        if not PixerImages.check_is_exist(image_id): return HttpResponseBadRequest("gallery not exists")
        if not PixerImages.check_is_author(image_id, uid): return HttpResponseBadRequest("permission denied")
        
        is_login, _, _ = PixerUser.user_validation(uid, session_id)
        if not is_login: return HttpResponseBadRequest("validation failed")
        
        try:
            image_manager = PixerImages.objects.filter(image_id=image_id)
            image_manager.delete()
            return HttpResponse("OK")
        except:
            return HttpResponseServerError("unknown error")
    
    return redirect("/gallery")

def download(request: HttpRequest):
    if request.method == "POST":
        uid = request.POST.get("uid")
        session_id = request.POST.get("session_id")
        image_id = request.POST.get("image_id")
        
        if uid is None: return HttpResponseBadRequest("key `uid` is required")
        if session_id is None: return HttpResponseBadRequest("key `session_id` is required")
        if image_id is None: return HttpResponseBadRequest("key `image_id` is required")
        
        # validation
        if not PixerImages.check_is_exist(image_id): return HttpResponseBadRequest("gallery not exists")
        
        is_login, _, _ = PixerUser.user_validation(uid, session_id)
        if not is_login: return HttpResponseBadRequest("validation failed")
        
        try:
            author_id = PixerImages.get_image_data(image_id).get("uid")
            
            if uid == author_id: return HttpResponse("OK")
            
            success = PixerWallet.change_pixel(uid, "buy")
            if not success: return HttpResponseBadRequest("not enough pixel to buy")
            
            success = PixerWallet.change_pixel(author_id, "sell")
            if not success: 
                PixerWallet.change_pixel(uid, "buy_failed")
                return HttpResponseServerError("unknown error")
            
            PixerImages.add_download_times(image_id)
            return HttpResponse("OK")
        except:
            return HttpResponseServerError("unknown error")
        
def image_page(request):
    return render(request, "image_page.html")