from PIL import ImageEnhance
from PIL.Image import Image
from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    category = models.CharField(max_length=100, db_index=True)

    def get_absolute_url(self):
        return reverse("cty_id", kwargs={'category_id': self.pk})

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']


class News(models.Model):
    # id = models.BigIntegerField(primary_key=True)
    caption = models.CharField(null=True, max_length=100, verbose_name="Заголовок")
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновленно")
    photo = models.ImageField(upload_to="news/%Y/%m/%d", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    likes = models.BigIntegerField(default=0)
    views = models.BigIntegerField(default=0)

    def hello(self):
        return "Hello word"

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse("one", kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['id']


class CustomUser(AbstractUser):
    likes = models.BigIntegerField(default=0)
    comments = models.BigIntegerField(default=0)

    photo = models.ImageField(upload_to="news/user/%Y/%m/%d", blank=True)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female")
    )
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)

    # add additional fields in here

    def __str__(self):
        return self.username


@receiver(pre_delete, sender=CustomUser)
def delete_photo(sender, instance=None, created=False, **kwargs):
    if instance.photo:
        storage, path = instance.photo.storage, instance.photo.path
        storage.delete(path)


# @receiver(post_save, sender=CustomUser)
# def delete_photo(sender, instance=None, created=False, **kwargs):
#     if instance.photo:
#         storage, path = instance.photo.storage, instance.photo.path
#
#     def transparency(filename1, filename2):
#         im = Image.open(filename1)
#         im1 = Image.open(filename2)
#         pixels = im.load()  # список с пикселями
#         pixels1 = im1.load()
#         x, y = im.size  # ширина (x) и высота (y) изображения
#         im0 = Image.new("RGB", (x, y), (0, 255, 0))
#         pixels0 = im0.load()
#
#         for i in range(x):
#             for j in range(y):
#                 r, g, b = pixels[i, j]
#                 r1, g1, b1 = pixels1[i, j]
#                 pixels0[i, j] = int(0.5 * r1 + 0.5 * r), int(0.5 * g1 + 0.5 * g), int(0.5 * b1 + 0.5 * b)
#
#         im0.save("res.jpg")
# а как дальше ?