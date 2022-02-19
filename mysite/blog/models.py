from django.db import models

class MyModel(models.Model):
    # id = models.BigIntegerField()
    caption = models.CharField(max_length=22,default=None)
    text = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="media/%Y/%m/%d", height_field=500, width_field=500,default="/media/img.png")
    is_published = models.BooleanField(default=True)