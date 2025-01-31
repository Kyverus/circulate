from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_modified = models.DateTimeField(User, auto_now=True)
    avatar = models.ImageField(default='avatars/default_avatar.png', blank=True, upload_to="avatars")
    banner = models.ImageField(default='profile_banners/default_banner.png', blank=True, upload_to="profile_banners")
    public_name = models.SlugField(max_length=60, blank=True)
    private = models.BooleanField(default=True)
    contact_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username
    
# Create User Profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance, public_name=instance.username.lower())
        user_profile.save()

# Automate Profile Creation
post_save.connect(create_profile, sender=User)
