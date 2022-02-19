from django.http import HttpResponse
from news.models import MyModel
from django.shortcuts import render

# Create your views here.

def test(request):
    print(request)
    news = MyModel.objects.all()
    #res = "<h1>Новости</h1>"
    #for i in news:
    #   res += f"\n<p>{i.caption}</p>\n<p>{i.text}</p>\n<p>{i.created_at}</p>\n<hr>"
    context = {
        "news": news,
        "title":"Список новостей"
    }
    return render(request,"news/test.html",context)

def test_new(request):
    return HttpResponse('Some text')