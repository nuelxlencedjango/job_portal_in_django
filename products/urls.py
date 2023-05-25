from django.urls import path
from .views import *
from .import views



app_name = 'products'


urlpatterns = [
    path('', views.index, name='home'),
  
    path('job-list/', views.jobListing, name='job-list'),
    path('job-detail/<int:pk>/', views.jobDetails, name='job-details'),
     path('manage-jobs/', views.manageJobsCreated, name='manage-jobs'),
     path('apply-job/', views.apply_to_job, name='apply-job'), 
    path('all-applicants/', views.all_applicants, name='all-applicants'),   
]
