from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(default="", null=False)
    private = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='post_banners/fallback.png', blank=True, upload_to="post_banners")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title