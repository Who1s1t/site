from django.http import HttpResponse
import datetime
from news.models import MyModel, Category
from django.shortcuts import render
from django.conf import settings


# Create your views here.

def test(request):
    print(request)
    news = MyModel.objects.all()
    ct = Category.objects.all()
    # res = "<h1>Новости</h1>"
    # for i in news:
    #   res += f"\n<p>{i.caption}</p>\n<p>{i.text}</p>\n<p>{i.created_at}</p>\n<hr>"
    context = {
        "categories": ct,
        "news": news,
        "title": "Список новостей"
    }
    return render(request, "news/test.html", context)


def archive(request):
    news = [i.strftime("%Y-%m-%d") for i in MyModel.objects.dates('created_at', "day", order='ASC')]
    context = {
        "news": news,
        "title": "Список новостей"
    }
    return render(request, "news/archive.html", context)


def archiveset(request):
    date = list(map(int, request.get_full_path()[9:-1].split('-')))
    print(date)
    news = MyModel.objects.filter(created_at__date=datetime.date(date[0], date[1], date[2]))
    print(news)
    context = {

        "news": news,
        "title": f"Список новостей {request.get_full_path()[9:-1]}"
    }
    return render(request, "news/test.html", context)


def get_category(request, category_id):
    news = MyModel.objects.filter(category=category_id)
    ct = Category.objects.all()
    context = {
        "categories": ct,
        "news": news,
        "title": Category.objects.get(pk=category_id).category
    }
    return render(request, "news/category_get.html", context)
