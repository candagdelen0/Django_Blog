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

def yurtdisi(request):
    outcities = Blog.objects.all().values()
    template3 = loader.get_template('pages/yurtdisi.html')
    context3 = {
        'outcities': outcities,
    }
    return HttpResponse(template3.render(context3, request))

def details(request, id):
    detay = Blog.objects.get(id=id)
    template = loader.get_template('pages/details.html')
    context = {
        'detay': detay,
    }
    return HttpResponse(template.render(context,request))

def advise(request):
    myadvise = Adviser.objects.all().values()
    template4 = loader.get_template('pages/oneriler.html')
    context = {
        'myadvise': myadvise,
    }
    return HttpResponse(template4.render(context,request))