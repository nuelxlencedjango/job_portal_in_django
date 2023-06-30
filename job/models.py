from django.db import models
from account.models import User
from cloudinary.models import CloudinaryField
from employers.models import Employers
from resume.models import *



class Location(models.Model):
   name = models.CharField(max_length=200)

   def __str__(self):
      return self.name


class Industry(models.Model):
   name = models.CharField(max_length=200)

   def __str__(self):
      return self.name


class AvailableJobs(models.Model):
   job_type_choices=(
      ('Remote','Remote'),
      ('Onsite','Onsite'),
      ('Hybrid','Hybrid')
   )
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   employers = models.ForeignKey(Employers, on_delete=models.CASCADE)
   #img = CloudinaryField(blank=True,null=True)
   title = models.CharField(max_length=200)
   city = models.CharField(max_length=200)
   location = models.ForeignKey(Location, on_delete=models.CASCADE,blank=True,null=True)
   salary = models.PositiveIntegerField(default=35000)
   requirements = models.TextField()
   ideal_candidate =models.TextField()
   is_available =models.BooleanField(default=True)
   date_created = models.DateField(auto_now_add = True, null=True, blank=True)
   created_on = models.DateTimeField(auto_now_add = True, null=True, blank=True)
   industry = models.ForeignKey(Industry, on_delete=models.CASCADE,blank=True,null=True)
   job_type= models.CharField(max_length=200,choices=job_type_choices,null=True,blank=True)


   class Meta:
      verbose_name_plural='AvailableJobs'
       
      ordering = ['-date_created']

   def __str__(self):
      return f"{self.title} - {self.employers}"
   



class ApplyJob(models.Model):
   status_choices=(
      ('Accepted','Accepted'),
      ('Declined','Declined'),
      ('Pending','Pending')
      )
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   job = models.ForeignKey(AvailableJobs, on_delete=models.CASCADE)
   timestamp =models.DateTimeField(auto_now_add=True)
   status = models.CharField(max_length=20, choices=status_choices)
   

   def __str__(self):
      return f"{self.user} - {self.job}"