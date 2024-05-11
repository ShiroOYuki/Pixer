from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from django.db.models import Manager
from User.models import PixerUser
from libs.utils import generate_uuid, encrypt_password

import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello User!")

def create_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # input columns check
        if username is None and email is None: return HttpResponseBadRequest("key `username` or `email` needs at least one")
        if password is None: return HttpResponseBadRequest("key `password` is required")
        
        # check is user exists
        if username is not None and PixerUser.objects.filter(username=username).exists(): return HttpResponseBadRequest("username already exists")
        if email is not None and PixerUser.objects.filter(email=email).exists(): return HttpResponseBadRequest("email already exists")

        # generate uid
        while True:
            timestamp = str(datetime.datetime.timestamp(datetime.datetime.now())).replace(".", "")
            if username is not None: uid = username + "_" + timestamp
            elif email is not None: uid = email.split("@")[0] + "_" + timestamp
            uid = generate_uuid(uid)
            if not PixerUser.objects.filter(uid=uid).exists(): 
                break
        
        is_superuser = False
        create_time = datetime.datetime.now()
        password = encrypt_password(password)
        print(len(password))
        
        try:
            new_user = PixerUser.objects.create(
                uid = uid,
                username = username,
                email = email,
                password = password,
                is_superuser = is_superuser,
                create_time = create_time
            )
        except Exception as e:
            return HttpResponseServerError("unknown error")
        
        return HttpResponse("OK")
    
    # 如果接收到的不是 POST 請求，就直接導回 /user
    return redirect("/user")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # input columns check
        if username is None and email is None: return HttpResponseBadRequest("key `username` or `email` needs at least one")
        if password is None: return HttpResponseBadRequest("key `password` is required")
        
        user:dict = None
        user_manager:Manager[PixerUser] = None
        password = encrypt_password(password)
        
        if username is not None:
            # login with username
            is_login, user_manager, user = PixerUser.login_with_username(username, password)
            if not is_login: return HttpResponseBadRequest("incorrect username or password")
        elif email is not None:
            # login with email
            is_login, user_manager, user = PixerUser.login_with_email(email, password)
            if not is_login: return HttpResponseBadRequest("incorrect email or password")
            
        try:
            uid = user.get("uid")
            login_time = datetime.datetime.now()
            user_manager.update(last_login=login_time)
            return JsonResponse({"uid": uid, "login_time": login_time})
        except:
            return HttpResponseServerError("unknown error")
    
    # 如果接收到的不是 POST 請求，就直接導回 /user
    return redirect("/user")
        