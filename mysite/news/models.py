from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']


class MyModel(models.Model):
    # id = models.BigIntegerField()
    caption = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновленно")
    photo = models.ImageField(upload_to="media/%Y/%m/%d", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def hello(self):
        return "Hello word"

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['id']
