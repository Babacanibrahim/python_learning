from django.shortcuts import render, HttpResponse , redirect , get_object_or_404
from . import forms
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request ,"about.html")

# Tüm Makaleler
def articles(request):
    keyword = request.GET.get("keyword")

    if keyword :
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html", {"articles":articles})


    articles = Article.objects.all()

    return render(request, "articles.html", {"articles":articles})

# Kontrol Paneli
@login_required(login_url="user:login")
def dashboard(request):
    articles =Article.objects.filter(author =request.user)
    context = {
        "articles" : articles
    }

    return render(request , "dashboard.html" , context)

# Makale Ekleme
@login_required(login_url="user:login")
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
    article = get_object_or_404(Article, id=id)
    context = {
        "article" : article
    }
    return render(request, "article.html" , context)

# Makele Güncelleme
@login_required(login_url="user:login")
def edit_article(request, id):
    article = get_object_or_404(Article, id = id , author = request.user)

    if request.method == "POST":
        form = forms.AddArticleForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.content = form.cleaned_data['content']
            article.save()
            messages.success(request, "Makale başarıyla güncellendi.")
            return redirect("article:dashboard")
    
    else:
        form = forms.AddArticleForm(initial={"title":article.title, "content":article.content})

    context = {
        "article": article,
        "form" : form
    }
    return render(request, "edit_article.html", context)

# Makale Silme
@login_required(login_url="user:login")
def delete_article(request, id):
    article = get_object_or_404(Article , id = id , author = request.user)

    if request.method == "POST":
        article.delete()
        messages.success(request, "Makaleniz başarıyla silindi.")
        return redirect("article:dashboard")
    
    return render(request,"dashboard.html")