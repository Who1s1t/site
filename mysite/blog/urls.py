from django.urls import path
from blog.views import search, ribbon, home

urlpatterns = [
    path('', home),
    path('search/', search),
    path('ribbon/', ribbon)
]
