

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
#from django.contrib.auth 
from django import forms
from .models import *


class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')







#class UserDetailForm(forms.ModelForm):
 #   class Meta:
  #      model = GrowthTrackRegistration
   #     fields = ('phone_no',)



#class UserLoginForm(AuthenticationForm):
 #   class Meta:
  #      model = User
   #     fields = ('username', 'password')