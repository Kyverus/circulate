from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

@login_required(login_url='/users/login/')
def post_create(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid:
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect("profile:index", request.user)
    else:
        form = forms.CreatePost()
    return render(request, "posts/post_create.html", {"form": form})

@login_required(login_url='/users/login/')
def post_update(request, post_slug):
    obj = Post.objects.get(slug=post_slug)

    form = forms.UpdatePost(instance=obj)
    if request.method == "POST":
        form = forms.UpdatePost(request.POST, request.FILES, instance=obj)
        if form.is_valid:
            form.save()
            return redirect("profile:index", request.user)
    return render(request, "posts/post_update.html", {"form": form, "post": obj})



