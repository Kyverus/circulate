from django import forms
from . import models


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['avatar','public_name', 'private','contact_number']