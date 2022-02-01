from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test(request):
    print(request)
    return HttpResponse('Hello, world!')

def test_new(request):
    return HttpResponse('Some text')