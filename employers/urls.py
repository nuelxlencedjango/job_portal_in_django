from django.urls import path
from .views import *
from .import views



app_name = 'employers'


urlpatterns = [
   path('update_company/', views.updateCompany, name='update_company'),
   path('detail_company/', views.emploerDetails, name='detail_company'),
]
