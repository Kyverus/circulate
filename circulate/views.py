from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q
from posts.models import Post

def home_page(request):
    if request.user.is_authenticated:
        posts = Post.objects.exclude(~Q(author=request.user), private=True).order_by('date')
    else:
        posts = Post.objects.filter(private=False)
    return render(request, "home_page.html", {"posts":posts})