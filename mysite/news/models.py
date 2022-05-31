from django.db import models
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
    #id = models.BigIntegerField(primary_key=True)
    caption = models.CharField(null=True,max_length=100, verbose_name="Заголовок")
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
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
