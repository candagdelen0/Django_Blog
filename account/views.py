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