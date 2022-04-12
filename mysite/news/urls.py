from django.urls import path
from news.views import archive, archiveset, get_category, add_news, news_one, ListNews
from news.models import MyModel

# TODO создаем файлик urls.py для разветвления
# Указываем:
urlpatterns = [
    path('', ListNews.as_view()),
    path('archive/', archive),
    path('category/<int:category_id>', get_category, name="cty_id"),
    path("add_news/", add_news, name="addn"),
    path("detail_news/<int:news_id>", news_one, name="one")
]
for i in [i.strftime("%Y-%m-%d") for i in MyModel.objects.dates('created_at', "day", order='ASC')]:
    urlpatterns.append(path(f'archive/{i}/', archiveset))
