from django.shortcuts import render
from django.http import HttpResponse

def search(request):
    return HttpResponse('Search :')
def ribbon(request):
    return HttpResponse("Ribbon")
def home(request):
    return render(request,'blog/index.html',)
