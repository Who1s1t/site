from django.db import models


class MyModel(models.Model):
    # id = models.BigIntegerField()
    caption = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновленно")
    photo = models.ImageField(upload_to="media/%Y/%m/%d", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['id']


class Category(models.Model):
    category = models.CharField(max_length=100, db_index=True)
    news = models.ForeignKey(MyModel, on_delete=models.CASCADE)
