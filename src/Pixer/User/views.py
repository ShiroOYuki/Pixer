from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from django.db.models import Manager
from User.models import PixerUser
from libs.utils.UserTools import check_email, generate_uuid, encrypt_password, generate_session_id

import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello User!")

<<<<<<< Updated upstream
def create_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # input columns check
        if username is None and email is None: return HttpResponseBadRequest("key `username` or `email` needs at least one")
        if password is None: return HttpResponseBadRequest("key `password` is required")
        if email is not None and not check_email(email): return HttpResponseBadRequest("invalid email")
        
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
        
        # create new user
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
        if email is not None and not check_email(email): return HttpResponseBadRequest("invalid email")
        if password is None: return HttpResponseBadRequest("key `password` is required")

        
        user:dict = None
        user_manager:Manager[PixerUser] = None
        if username is not None:
            # login with username
            is_login, user_manager, user = PixerUser.login_with_username(username, password)
            if not is_login: return HttpResponseBadRequest("incorrect username or password")
        elif email is not None:
            # login with email
            is_login, user_manager, user = PixerUser.login_with_email(email, password)
            if not is_login: return HttpResponseBadRequest("incorrect email or password")
        
        # user login
        try:
            uid = user.get("uid")
            login_time = datetime.datetime.now()
            session_id = generate_session_id()
            user_manager.update(last_login=login_time, session_id=session_id)
            return JsonResponse({"uid": uid, "login_time": login_time, "session_id": session_id})
        except:
            return HttpResponseServerError("unknown error")
    
    # 如果接收到的不是 POST 請求，就直接導回 /user
    return redirect("/user")
        
def update_user(request):
    if request.method == "POST":
        # used for validation
        uid = request.POST.get("uid")
        session_id = request.POST.get("session_id")
        old_password = request.POST.get("old_password")
        
        # columns needs to be update
        username = request.POST.get("username")
        email = request.POST.get("email")
        new_password = request.POST.get("new_password")
        
        # input columns check
        if uid is None: return HttpResponseBadRequest("key `uid` is required")
        if session_id is None: return HttpResponseBadRequest("key `session_id` is required")
        if old_password is None: return HttpResponseBadRequest("key `old_password` is required")
        if username is None and email is None and new_password is None: return HttpResponseBadRequest("key `username`, `email` or `new_password` needs at least one")
        if email is not None and not check_email(email): return HttpResponseBadRequest("invalid email")

        # validation
        is_login, user_manager, user = PixerUser.login_with_uid(uid, session_id, old_password)
        if not is_login: return HttpResponseBadRequest("login failed")
        
        # check is user exists
        if username is not None and PixerUser.objects.filter(username=username).exists(): return HttpResponseBadRequest("username already exists")
        if email is not None and PixerUser.objects.filter(email=email).exists(): return HttpResponseBadRequest("email already exists")
        
        # update user
        try:
            if not username: username = user.get("username")
            if not email: email = user.get("email")
            user_manager.update(
                username = username,
                email = email
            )
            if new_password is not None: user_manager.update(password=encrypt_password(new_password))
        except Exception as e:
            return HttpResponseServerError("unknown error")
        
        return HttpResponse("OK")
    
    # 如果接收到的不是 POST 請求，就直接導回 /user
    return redirect("/user")

def get_user_data(request):
    if request.method == "POST":
        uid = request.POST.get("uid")
        session_id = request.POST.get("session_id")
        targets = request.POST.getlist("targets[]")
        
        if uid is None: return HttpResponseBadRequest("key `uid` is required")
        if session_id is None: return HttpResponseBadRequest("key `session_id` is required")
        if targets is None: return HttpResponseBadRequest("key `targets` is required")
        
        # validation
        is_login, _, user = PixerUser.user_validation(uid, session_id)
        if not is_login: return HttpResponseBadRequest("login failed")
        
        try:
            res = dict()
            for target in targets:
                res[target] = user.get(target)
                
            return JsonResponse(res)
        except:
            return HttpResponseServerError("unknown error")
        
        
    # 如果接收到的不是 POST 請求，就直接導回 /user
    return redirect("/user")
=======
def login_page(request):
    return render(request, "login.html")
>>>>>>> Stashed changes
