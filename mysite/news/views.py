from django.http import HttpResponse
import datetime

from django.views.generic import ListView, DetailView, CreateView

from news.models import News, Category
from django.shortcuts import render, redirect
from news.forms import AddNewsForm
from django.conf import settings




class ListNews(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news"

    # extra_context = {"title":"Новости","categories":ct_get()}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новости"
        return context


class GetCat(ListView):
    template_name = "news/news_list.html"
    context_object_name = "news"

    def get_queryset(self, **kwargs):
        return News.objects.filter(category=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(pk=self.kwargs["category_id"]).category
        return context

class DetailNews(DetailView):
    model = News
    template_name = "news/news_one.html"
    context_object_name = "news"
    # pk_url_kwarg = 'news_id'

class AddNews(CreateView):
    model = News
    form_class = AddNewsForm
    template_name = "news/add_news.html"

def archive(request):
    news = [i.strftime("%Y-%m-%d") for i in News.objects.dates('created_at', "day", order='ASC')]
    context = {
        "news": news,
        "title": "Список новостей"
    }
    return render(request, "news/archive.html", context)


def archiveset(request):
    date = list(map(int, request.get_full_path()[9:-1].split('-')))
    print(date)
    news = News.objects.filter(created_at__date=datetime.date(date[0], date[1], date[2]))
    print(news)
    context = {

        "news": news,
        "title": f"Список новостей {request.get_full_path()[9:-1]}"
    }
    return render(request, "news/test.html", context)


# def add_news(request):
#     if request.method == 'POST':
#         form = AddNewsForm(request.POST)  # тут все круто
#         if form.is_valid():
#             news = form.save()
#             return redirect(news)
#     else:
#         form = AddNewsForm()
#     return render(request, "news/add_news.html", {"categories": ct_get(), "form": form})
#
#
# def news_one(request, news_id):
#     news = News.objects.get(pk=news_id)
#     context = {
#         "news": news
#     }
#     return render(request, "news/news_one.html", context)
