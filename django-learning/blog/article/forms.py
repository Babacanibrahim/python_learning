from django import forms
from ckeditor.fields import RichTextField
from .models import Comment

class AddArticleForm(forms.Form):
    title = forms.CharField(label ="Makale Başlığı")
    content = forms.CharField(label = "Makale İçeriği", widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_author", "comment_content"]
        widgets = {
            'comment_author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adınızı girin'
            }),
            'comment_content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Yorumunuzu yazın...',
                'rows': 4
            }),
        }
        labels = {
            'comment_author': 'Adınız',
            'comment_content': 'Yorumunuz',
        } 