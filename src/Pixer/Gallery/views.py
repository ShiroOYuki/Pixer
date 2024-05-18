from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

from libs.utils.GalleryTools import get_image_data
from libs.utils.UserTools import generate_session_id
from Gallery.models import PixerImages, PixerFavorites
from User.models import PixerUser

# Create your views here.
def index(request):
    return HttpResponse("Hello Gallery!")

def image_page(request, image_id:str):
    uid = request.GET.get("uid") # 在網址後面接 ?uid=<your_uid>
    print(uid)
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