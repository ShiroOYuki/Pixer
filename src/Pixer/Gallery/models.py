# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PixerGallery(models.Model):
    gallery_id = models.CharField(primary_key=True, max_length=40, db_collation='utf8mb3_bin')
    image_id = models.CharField(unique=True, max_length=40)
    download_times = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=45, db_collation='utf8mb3_bin', blank=True, null=True)
    description = models.CharField(max_length=100, db_collation='utf8mb3_bin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pixer_gallery'
