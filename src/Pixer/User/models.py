# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import Manager
from libs.utils.UserTools import check_password

class PixerUser(models.Model):
    uid = models.CharField(primary_key=True, max_length=20)
    username = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=45)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    session_id = models.CharField(max_length=36, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'pixer_user'
        ordering = ['-create_time', "username"]
    
    @classmethod
    def login_with_username(cls, username: str, password: str) -> tuple[bool, Manager["PixerUser"], dict]:
        # login with username
        user_manager = cls.objects.filter(username=username)
        if not user_manager.exists(): return False, None, None
        
        # case-sensitive check
        user = user_manager.values().first()
        if user.get("username") != username or not check_password(password, user.get("password")): 
            return False, None, None
        
        return True, user_manager, user
    
    @classmethod
    def login_with_email(cls, email: str, password: str) -> tuple[bool, Manager["PixerUser"], dict]:
        # login with username
        user_manager = cls.objects.filter(email=email)
        if not user_manager.exists(): return False, None, None
        
        # case-sensitive check
        user = user_manager.values().first()
        if user.get("email") != email or not check_password(password, user.get("password")):  
            return False, None, None
        
        return True, user_manager, user
    
    @classmethod
    def login_with_uid(cls, uid: str, session_id: str, password: str) -> tuple[bool, Manager["PixerUser"], dict]:
        # login with username
        user_manager = cls.objects.filter(uid=uid, session_id=session_id)
        if not user_manager.exists(): return False, None, None
        
        # case-sensitive check
        user = user_manager.values().first()
        if user.get("uid") != uid or not check_password(password, user.get("password")):  
            return False, None, None
        
        return True, user_manager, user
    
    @classmethod
    def user_validation(cls, uid: str, session_id:str) -> tuple[bool, Manager["PixerUser"], dict]:
        # login with username
        user_manager = cls.objects.filter(uid=uid, session_id=session_id)
        if not user_manager.exists(): return False, None, None
        
        user = user_manager.values().first()
        
        return True, user_manager, user