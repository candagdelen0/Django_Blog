from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User


def user_login(request):
    if  request.user.is_authenticated:
        return  redirect("/")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return  redirect("/")
        else:
            return  render(request, "account/login.html",{"error":"username ya da parola hatalı"})
    else:
        return render(request, "account/login.html")

def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password != repassword:
            return  render (request, "account/register.html", {
                "error": "Girilen Parolalar Eşleşmiyor",
                "username":username,
                "email": email
            })

        if User.objects.filter(username=username).exists():
            return render(request,"account/register.html", {
                "error": "Kullanıcı Adı Kullanıyor",
                "username": username,
                "email": email
            })

        if User.objects.filter(email=email).exists():
            return render(request, "account/register.html", {
                "error": "E-mail Kullanıyor",
                "username": username,
                "email": email
            })
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return  redirect("user_login")
    return render(request, "account/register.html")

def user_logout(request):
    logout(request)
    return redirect("/")