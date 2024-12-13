from .models import Article
from django import forms


class CreateArt(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "artImage", "desc", "content", "category"]
        labels = {
            "title": "Заголовок статьи",
            "artImage": "Изображение",
            "desc": "Описание",
            "content": "Содержание",
            "category": "Категории",
        }
        # widgets = {
        #   'title': forms.TextInput(attrs = {'class': 'dark-form form-control'}),
        #   'category': forms.CheckboxSelectMultiple(attrs= {'class': 'form-check-input category-select'}),
        #   }
