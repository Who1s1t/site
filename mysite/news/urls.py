from django.urls import path
from news.views import archive, archiveset, GetCat, ListNews,DetailNews,AddNews,AddUser
from news.models import News

# TODO создаем файлик urls.py для разветвления
# Указываем:
urlpatterns = [
    path('', ListNews.as_view()),
    path('archive/', archive),
    path('category/<int:category_id>', GetCat.as_view(), name="cty_id"),
    path("add_news/", AddNews.as_view(), name="addn"),
    path("detail_news/<int:pk>", DetailNews.as_view(), name="one"),
    path("add_user/", AddUser.as_view(), name="addu")

]
for i in [i.strftime("%Y-%m-%d") for i in News.objects.dates('created_at', "day", order='ASC')]:
    urlpatterns.append(path(f'archive/{i}/', archiveset))
