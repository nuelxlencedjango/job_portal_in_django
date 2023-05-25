from django.urls import path
from .views import *
from .import views



app_name = 'job'


urlpatterns = [
   path('create-job/', views.create_job, name='create-job'),
   path('update-job/<int:pk>/', views.updateJob, name='update-job'),
    path('applied-jobs/', views.applied_jobs, name='applied-jobs'),
]
