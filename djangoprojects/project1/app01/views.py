from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request): # request can be any word
    return HttpResponse("<em>Hello Africa</em>")