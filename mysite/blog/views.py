from django.shortcuts import render
from django.http import HttpResponse

def search():
    return HttpResponse('Search :')
def ribbon():
    return HttpResponse("Ribbon")
def home():
    return HttpResponse("Home")
