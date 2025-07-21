from django import forms
from ckeditor.fields import RichTextField

class AddArticleForm(forms.Form):
    title = forms.CharField(label ="Makale Başlığı")
    content = forms.CharField(label = "Makale İçeriği", widget=forms.Textarea)