
from django import forms
from .models import *


class CreateJobForm(forms.ModelForm):

    class Meta:
        model = AvailableJobs
        exclude = ('user', 'employers','date_created','is_available')



class JobUpdateForm(forms.ModelForm):

    class Meta:
        model = AvailableJobs
        exclude = ('user', 'employers','date_created','is_available')