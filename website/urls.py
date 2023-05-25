from django.urls import path
from .views import *
from .import views



app_name = 'website'


urlpatterns = [
  # path('create-job/', views.create_job, name='create-job'),
   #path('update-job/<int:pk>/', views.updateJob, name='update-job'),
]
