from django import forms
from .models import Blogs

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'slug', 'description', 'image']
