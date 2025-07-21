from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

# Register
def register(request):
    form = forms.RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.success(request, "Başarılıyla giriş yapıldı.")
        return redirect("index")

    context = {
        "form" : form
    }

    return render(request,"register.html" , context)


# Login
def loginUser(request):
    form = forms.LoginForm(request.POST or None)
    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username , password = password)

        if user is None:
            messages.info(request, "Kullanıcı adı veya parola hatalı")
            return render(request, "login.html", context)

        login(request, user)
        messages.success(request, "Giriş başarıyla yapıldı")
        return redirect( "index")
    
    return render(request,"login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request , "Başarıyla çıkış yapıldı")
    return redirect("user:login")