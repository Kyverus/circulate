from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','private','slug','banner']

class UpdatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','private','slug','banner']
