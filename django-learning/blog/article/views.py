from django.shortcuts import render, HttpResponse , redirect , get_object_or_404
from . import forms
from django.contrib import messages
from .models import Article
import time

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request ,"about.html")

# Kontrol Paneli
def dashboard(request):
    articles =Article.objects.filter(author =request.user)
    context = {
        "articles" : articles
    }

    return render(request , "dashboard.html" , context)

# Makale Ekleme
def addarticle(request):
    form  = forms.AddArticleForm(request.POST or None)
    context = {
       "form": form
    }

    if form.is_valid():
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        newArticle = Article(title = title, content = content , author = request.user)
        newArticle.save()
        messages.success(request ,"Makalen başarılı şekilde eklendi.")
        return redirect("/articles/dashboard")
    return render(request , "addarticle.html" , context)

# Makale Detay
def article(request, id):
    article = get_object_or_404(Article, id=id, author=request.user)
    context = {
        "article" : article
    }
    return render(request, "article.html" , context)