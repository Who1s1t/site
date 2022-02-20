from django.urls import path
from news.views import test, archive, archiveset
from news.models import MyModel

# TODO создаем файлик urls.py для разветвления
# Указываем:
urlpatterns = [
    path('', test),
    path('archive/', archive)
]
for i in [i.strftime("%Y-%m-%d") for i in MyModel.objects.dates('created_at', "day", order='ASC')]:
    urlpatterns.append(path(f'archive/{i}/', archiveset))
