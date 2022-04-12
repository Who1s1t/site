from django.urls import path
from news.views import test, archive, archiveset, get_category, add_news, news_one
from news.models import MyModel

# TODO создаем файлик urls.py для разветвления
# Указываем:
urlpatterns = [
    path('', test),
    path('archive/', archive),
    path('category/<int:category_id>', get_category, name="cty_id"),
    path("add_news/", add_news, name="addn"),
    path("<int:news_id>", news_one, name="one") # тут лучше уточнить маршрут, а то непонятно что получаем (всм добавить что-то типа detail_news/<int:news_id>)
]
for i in [i.strftime("%Y-%m-%d") for i in MyModel.objects.dates('created_at', "day", order='ASC')]:
    urlpatterns.append(path(f'archive/{i}/', archiveset))
