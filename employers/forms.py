
from django import forms

#from django.forms import widgets

from .models import *



class UpdateCompanyForm(forms.ModelForm):

    class Meta:
        model = Employers
        exclude =('user',)
