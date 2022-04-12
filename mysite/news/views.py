from django.http import HttpResponse
import datetime
from news.models import MyModel, Category
from django.shortcuts import render
from news.forms import Add_newsForm
from django.conf import settings


def ct_get():
    return Category.objects.all()


# Create your views here.

def test(request):
    print(request)
    news = MyModel.objects.all()
    ct = ct_get()
    context = {
        "categories": ct,
        "news": news,
        "title": "Список новостей"
    }
    return render(request, "news/news_list.html", context)


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
    ct = ct_get()
    context = {
        "categories": ct,
        "news": news,
        "title": Category.objects.get(pk=category_id).category
    }
    return render(request, "news/news_list.html", context)


def add_news(request):
    if request.method == 'POST':
        form = Add_newsForm(request.POST)  # тут все круто
        if form.is_valid():
            print(form.cleaned_data["caption"])
            print(form.cleaned_data["text"])
            print(form.cleaned_data["is_published"])
            print(form.cleaned_data["category"])
            # form.save()
    else:
        form = Add_newsForm()
    return render(request, "news/add_news.html", {"categories": ct_get(), "form": form})


def news_one(request, news_id):
    news = MyModel.objects.filter(pk=news_id)  # тут тебе cкорее не filter нужен, а get
    ct = ct_get()
    context = {
        "categories": ct,
        "news": news
    }
    return render(request, "news/news_list.html", context)
