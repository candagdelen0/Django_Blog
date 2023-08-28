from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Blog, Adviser
from django.core.paginator import Paginator

def index(request):
    cities = Blog.objects.all().values()
    template = loader.get_template('pages/index.html')
    context = {
        'cities': cities,
    }
    return HttpResponse(template.render(context, request))

def yurtici(request):
    incities = Blog.objects.filter(ulkeAdi='Türkiye').values()
    template2 = loader.get_template('pages/yurtici.html')
    context2 = {
        'incities' : incities,
    }
    return HttpResponse(template2.render(context2, request))