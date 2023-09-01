from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Blog, Adviser
from django.core.paginator import Paginator
from pages.forms import TextCreateForm, AdviseCreateForm

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

def advisedetail(request, id):
    adetay = Adviser.objects.get(id=id)
    template = loader.get_template('pages/advisedetails.html')
    context = {
        'adetay' : adetay,
    }
    return HttpResponse(template.render(context, request))

def create_text(request):
    if request.method == "POST":
        form = TextCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  redirect("/")
    else:
        form = TextCreateForm()
    return  render(request, "pages/create-text.html", {"form":form})

def create_advise(request):
    if request.method == "POST":
        form = AdviseCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = AdviseCreateForm()
    return render(request, "pages/create-advise.html",{"form":form})

def yazi_listesi(request):
    liste = Blog.objects.all()
    liste2 = Adviser.objects.all()
    return render(request, 'pages/yazi-listesi.html', {"liste": liste, "liste2": liste2})

def text_edit(request, id):
    mytext = get_object_or_404(Blog, pk=id)
    if request.method == "POST":
        form = TextCreateForm(request.POST, request.FILES, instance=mytext)
        form.save()
        return redirect("/yazi-listesi")
    else:
        form = TextCreateForm(instance=mytext)
    return render(request, 'pages/edit-text.html',{"form":form})

def advise_edit(request, id):
    myadv = get_object_or_404(Adviser, pk=id)
    if request.method == "POST":
        form2 = AdviseCreateForm(request.POST, request.FILES, instance=myadv)
        form2.save()
        return redirect("/yazi-listesi")
    else:
        form2 = AdviseCreateForm(instance=myadv)
    return render(request, 'pages/edit-advise.html', {"form2": form2})

def text_delete(request, id):
    mytext = get_object_or_404(Blog, pk=id)
    if request.method == "POST":
        mytext.delete()
        return redirect("/yazi-listesi")
    return render(request, 'pages/delete-text.html', {"mytext": mytext})

def advise_delete(request, id):
    myadv = get_object_or_404(Adviser, pk=id)
    if request.method == "POST":
        myadv.delete()
        return  redirect("/yazi-listesi")
    return render(request,'pages/delete-advise.html', {"myadv":myadv})

