from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content', 'image']  # Make sure 'create_at' is in the model
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your title.....'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your content.....'
            }),
        }
