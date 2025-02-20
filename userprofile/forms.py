from django import forms
from . import models


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['avatar', 'banner','public_name', 'private','contact_number']