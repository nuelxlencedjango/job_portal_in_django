from django.urls import path
from .views import *
from .import views

#from django.contrib.auth import views as auth_views



app_name = 'account'


urlpatterns = [

    path('artisan_register/',views.artisans_registration, name ='artisan_register'),
    path('employer_register/',views.employer_registration, name ='employer_register'),
    path('login/' ,views.loginPage , name='login'),


   
    path('logout/', views.logoutPage, name='logout'),
  

]
