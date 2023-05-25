
from django import forms

#from django.forms import widgets

from .models import *



class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        exclude =('user','date_created')
