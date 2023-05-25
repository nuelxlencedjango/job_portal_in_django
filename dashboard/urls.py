from django.urls import path
from .views import *
from .import views

#from django.contrib.auth import views as auth_views



app_name = 'dashboard'


urlpatterns = [
    path('dashboards/',views.users_dashboard,name ='dashboards'),
    #path('artisan-dashboard/',views.artisanDashboard,name ='artisan-dashboard'),
    #path('employer-dashboard/',views.employerDashboard,name ='employer-dashboard'),
      
]
