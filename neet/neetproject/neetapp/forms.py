from django import forms
from django.forms import fields, models
from .models import Member

class MemberForm(models.ModelForm):
    class Meta:
        model = Member
        fields = ['title','title_image','body']