from django.db import models
from account.models import User
from cloudinary.models import CloudinaryField

#from artisan.models import Artisan

class Resume(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   img = CloudinaryField(blank=True,null=True)
   first_name = models.CharField(max_length=200)
   surname = models.CharField(max_length=200)
   location = models.CharField(max_length=200)
   job_title = models.CharField(max_length=200)
   upload_resume =models.FileField(upload_to='resume',null=True, blank=True)
   date_created = models.DateField(auto_now_add = True, null=True, blank=True)
   class Meta:
      verbose_name_plural='Resume'
       
      ordering = ['-date_created']

   def __str__(self):
      return f"{self.first_name} - {self.surname}"

     

  