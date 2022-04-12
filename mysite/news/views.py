from django.http import HttpResponse
import datetime

from django.views.generic import ListView

from news.models import MyModel, Category
from django.shortcuts import render, redirect
from news.forms import AddNewsForm
from django.conf import settings


def ct_get():
    return Category.objects.all()

class ListNews(ListView):
    model = MyModel
    template_name = "news/news_list.html"
    context_object_name = "news"
    #extra_context = {"title":"Новости","categories":ct_get()}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новости"
        return context



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
        form = AddNewsForm(request.POST)  # тут все круто
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = AddNewsForm()
    return render(request, "news/add_news.html", {"categories": ct_get(), "form": form})


def news_one(request, news_id):
    news = MyModel.objects.filter(pk=news_id)
    ct = ct_get()
    context = {
        "categories": ct,
        "news": news
    }
    return render(request, "news/news_list.html", context)
