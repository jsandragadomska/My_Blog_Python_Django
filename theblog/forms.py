from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'snippet', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your title here'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user_id', 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your snippet here'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your snippet here'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

