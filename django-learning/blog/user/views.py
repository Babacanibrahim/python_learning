from django.shortcuts import render
from . import forms

# Create your views here.

def register(request):
    form = forms.RegisterForm()
    context = {
        "form" : form
    }

    return render(request,"register.html" , context)

def login(request):
    return render(request,"login.html")


def logout(request):
    pass