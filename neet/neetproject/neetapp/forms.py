from django import forms
from django.forms import fields, models
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['title','writer','body', 'num']