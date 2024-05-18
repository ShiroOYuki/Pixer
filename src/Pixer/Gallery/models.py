# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PixerImages(models.Model):
    image_id = models.CharField(primary_key=True, max_length=40, db_collation='utf8mb4_bin')
    uid = models.CharField(max_length=20, db_collation='utf8mb4_bin')
    filepath = models.CharField(max_length=100, db_collation='utf8mb4_bin')
    create_time = models.DateTimeField(blank=True, null=True)
    format = models.CharField(max_length=10, db_collation='utf8mb4_bin', blank=True, null=True)
    download_times = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pixer_images'
        
    @classmethod
    def get_image_data(cls, image_id:str):
        data = cls.objects.filter(image_id=image_id)
        if not data.exists(): return None
        
        return data.values().first()
    
    
    
class PixerFavorites(models.Model):
    favorite_id = models.CharField(primary_key=True, max_length=45)
    image_id = models.CharField(max_length=45)
    uid = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'pixer_favorites'