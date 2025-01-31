from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from posts.models import Post
from .models import Profile
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request, public_name):
    profile = Profile.objects.get(public_name=public_name)
    user = User.objects.get(profile=profile)
    userProfile = Profile.objects.get(user=user)

    if userProfile.user == request.user:
        profileDetails = userProfile
        print("match")
    else:
        print("not match")
        if userProfile.private:
            profileDetails = {"avatar": userProfile.avatar, "banner": userProfile.banner, "public_name": userProfile.public_name, "private": userProfile.private}
            print("private")
        else:
            profileDetails = userProfile
            print("not private")
        
    if userProfile.user == request.user:
        posts = Post.objects.filter(author=user)
    else:
        posts = Post.objects.filter(author=user, private=False)
    return render(request, "profile/profile_index.html", {"posts": posts, "profileDetails": profileDetails})

@login_required(login_url='/users/login/')
def update(request):
    obj = Profile.objects.get(user=request.user)
    form = forms.UpdateProfile(instance=obj)
    if request.method == "POST":
        form = forms.UpdateProfile(request.POST,request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("profile:index", request.user.profile.public_name)
    return render(request, "profile/profile_update.html", {"form": form})