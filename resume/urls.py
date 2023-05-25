from django.urls import path
from .views import *
from .import views



app_name = 'resume'


urlpatterns = [
  path('resume_update/',views.updateResume, name ='resume_update'),
    path('resume_details/',views.resumeDetails, name ='resume_details'),
    
]
