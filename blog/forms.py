# blog/forms.py
from django import forms
from .models import Post, Comment, HashTag

# Form

# Model Form 
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']


class HashTagForm(forms.ModelForm):

    class Meta:
        model = HashTag
        fields = ['name']
