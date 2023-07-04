from django.urls import path
from .views import *
from .import views



app_name = 'products'


urlpatterns = [
    path('', views.index, name='home'),
  
    path('job-list/', views.jobListing, name='job-list'),
    path('job-details/<int:pk>/', views.jobDetails, name='job-details'),
     path('manage-jobs/', views.manageJobsCreated, name='manage-jobs'),
     path('apply-job/<int:pk>/', views.apply_to_job, name='apply-job'), 
      path('company_jobs/', views.companyJobs, name='company_jobs'),

    path('all-applicants/<int:pk>/', views.all_applicants, name='all-applicants'),  

     path('accepted/<int:pk>/', views.decisionAccept, name='accepted'), 
    path('decline/<int:pk>/', views.declinedApplication, name='declined'), 
]
