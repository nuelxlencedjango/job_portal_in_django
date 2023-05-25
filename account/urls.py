from django.urls import path
from .views import *
from .import views

#from django.contrib.auth import views as auth_views



app_name = 'account'


urlpatterns = [

    path('artisan-register/',views.artisans_registration, name ='artisan-register'),
    path('employer_register/',views.employer_registration, name ='employer_register'),
    path('login/' ,views.loginPage , name='login'),

    #path('admin_page/',views.adminPage ,name='admin_page'),
   # path('update_info/', views.update_info, name="update_info"),
   
    path('logout/', views.logoutPage, name='logout'),
  

]
