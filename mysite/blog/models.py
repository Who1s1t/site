from django.db import models

class MyModel(models.Model):
    # id = models.BigIntegerField()
    email = models.EmailField(max_length=100,default=None)
    password = models.CharField(max_length=100,default=None)
    caption = models.CharField(max_length=22,default=None)
    text = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photo/", height_field=500, width_field=500,default="/photo/img.png")
    is_published = models.BooleanField(default=True)
    subscribers = models.BigIntegerField(default=0)
    like = models.BigIntegerField(default=0)
    donate = models.FloatField(default=0)
    Publications = models.BigIntegerField(default=0)