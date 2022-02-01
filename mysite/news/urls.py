from django.urls import path
from news.views import test,test_new
#TODO создаем файлик urls.py для разветвления
# Указываем:
urlpatterns = [
    path('', test),
    path('test/', test_new),
]
