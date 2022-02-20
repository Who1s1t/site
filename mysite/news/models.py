from django.db import models


class MyModel(models.Model):
    # id = models.BigIntegerField()
    caption = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="media/", height_field=500, width_field=500)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.caption
