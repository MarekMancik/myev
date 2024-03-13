from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'source', 'author', 'category', 'tags']
        widgets = {'content': CKEditorWidget()}